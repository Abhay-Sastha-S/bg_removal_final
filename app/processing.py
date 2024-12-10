from PIL import Image
import torch
import torch.nn.functional as F
import numpy as np
from .u2net.u2net import U2NET
from .config import U2NET_WEIGHTS

u2net_model = None

def load_u2net_model():
    global u2net_model
    if u2net_model is None:
        u2net_model = U2NET(3,1)
        u2net_model.load_state_dict(torch.load(U2NET_WEIGHTS, map_location=torch.device('cpu')))
        u2net_model.eval()

def norm_pred(d):
    ma = torch.max(d)
    mi = torch.min(d)
    dn = (d - mi)/(ma - mi)
    return dn

def segment_foreground(img):
    load_u2net_model()
    img_rgb = img.convert("RGB")
    tensor = torch.from_numpy(np.array(img_rgb)).permute(2,0,1).unsqueeze(0).float()/255.0

    with torch.no_grad():
        d1, d2, d3, d4, d5, d6, d7 = u2net_model(tensor)
        pred = d1[:,0,:,:]
        pred = norm_pred(pred)
    
    mask_np = (pred.detach().cpu().numpy()*255).astype(np.uint8)
    mask_img = Image.fromarray(mask_np, mode='L')
    return mask_img

def remove_background(image_path, bbox):
    original = Image.open(image_path).convert("RGBA")
    cropped = original.crop((bbox.x_min, bbox.y_min, bbox.x_max, bbox.y_max))
    mask = segment_foreground(cropped)

    transparent_img = Image.new("RGBA", cropped.size, (0,0,0,0))
    transparent_img = Image.composite(cropped, transparent_img, mask)
    
    out_path = "/tmp/output_image.png"
    transparent_img.save(out_path, "PNG")
    return out_path
