import numpy as np

class Bounding_box:
    def __init__(self, x1, y1, x2, y2, score):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.score = score

def get_iou(boxa, boxb):
    max_x = max(boxa.x1, boxb.x1)
    max_y = max(boxa.y1, boxb.y1)
    min_x = min(boxa.x2, boxb.x2)
    min_y = min(boxa.y2, boxb.y2)
    if min_x <= max_x or min_y <= max_y:
        return 0
    area_i = (min_x - max_x) * (min_y - max_y)
    area_a = (boxa.x2 - boxa.x1) * (boxa.y2 - boxa.y1)
    area_b = (boxb.x2 - boxb.x1) * (boxb.y2 - boxb.y1)
    area_u = area_a + area_b - area_i
    return float(area_i) / float(area_u)

def NMS(box_lists, k):
    box_lists = sorted(box_lists, key=lambda x: x.score, reverse=True)
    NMS_lists = [box_lists[0]]
    temp_lists = []
    for i in range(k):
        for j in range(1, len(box_lists)):
            iou = get_iou(NMS_lists[i], box_lists[j])
            if iou < 0.7:
                temp_lists.append(box_lists[j])
        if len(temp_lists) == 0:
            return NMS_lists
        box_lists = temp_lists
        temp_lists = []
        NMS_lists.append(box_lists[0])
    return NMS_lists

box1 = Bounding_box(13, 22, 268, 367, 0.124648176)
box2 = Bounding_box(18, 27, 294, 400, 0.35818103)
box3 = Bounding_box(234, 123, 466, 678, 0.13638769)
box_lists = [box1, box2, box3]
NMS_list = NMS(box_lists, 2)
print NMS_list
print NMS_list[0].x1