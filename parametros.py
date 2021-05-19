import torch
from torchinfo import summary
import json
import trt_pose.coco
import trt_pose.models
from flopth import flopth

with open('human_pose.json', 'r') as f:
    human_pose = json.load(f)

topology = trt_pose.coco.coco_category_to_topology(human_pose)
num_parts = len(human_pose['keypoints'])
num_links = len(human_pose['skeleton'])

model = trt_pose.models.resnet18_baseline_att(num_parts, 2 * num_links).cuda().eval()

model.load_state_dict(torch.load('resnet18_baseline_att_224x224_A_epoch_249.pth'))
summary(model)
#print(model.fc1.in_features)
sum_flops = flopth(model,in_size=[[3,224,224]])
print(sum_flops)
