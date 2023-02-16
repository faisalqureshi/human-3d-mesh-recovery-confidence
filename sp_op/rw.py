import numpy as np
import torch
import sys
sys.path.insert(0, '/SPINH')


dataset_index = 0
occluded = False
dataset_name = ["3dpw", "h36m-p1", "h36m-p2", "mpi-inf-3dhp", "3doh"]
dataset = dataset_name[dataset_index]
if occluded:
    path = "sp_op/" + dataset + "/" + dataset + "_occ_"
else:
    path = "sp_op/" + dataset + "/" + dataset + "_"
print(path)
sp_op = np.load(path + 'sp_op.npy')
sp_gt = np.load(path + 'sp_gt.npy')
sp_op = torch.tensor(sp_op)
sp_gt = torch.tensor(sp_gt)


a = [max(i) for i in sp_gt]
b = [min(i) for i in sp_gt]
c = [max(i) for i in sp_op]
d = [min(i) for i in sp_op]
j=10
print(a[j]-b[j])
print(c[j]-d[j])

# sp_gt_max_ind = torch.argmax(sp_gt, dim=1)
# sp_gt_min_ind = torch.argmin(sp_gt, dim=1)
# sp_gt_max = sp_gt[range(len(sp_gt)), sp_gt_max_ind]
# sp_gt_min = sp_gt[range(len(sp_gt)), sp_gt_min_ind]
# diff = sp_gt_max - sp_gt_min
# ind = (diff > 0.15).nonzero().squeeze(1)
# sp_gt_new = torch.index_select(sp_gt, 0, ind)
# sp_op_new = torch.index_select(sp_op, 0, ind)
# print(sp_op_new.shape)

# ##### Model 1 GT 1
# sp_op_max_ind = torch.argmax(sp_op, dim=1)
# sp_gt_max_ind = torch.argmax(sp_gt, dim=1)
# eval = torch.eq(sp_op_max_ind, sp_gt_max_ind)
# eval = eval.cpu().numpy()
# print(100 * eval.mean())


# ###### Model 2 GT 1
# sp_gt_max_ind = torch.argmax(sp_gt, dim=1)
# _, sp_op_max_ind = torch.topk(sp_op, 3)
# eval = torch.zeros(len(sp_gt_max_ind))
# for i in range(len(sp_gt_max_ind)):
#     if sp_gt_max_ind[i] in sp_op_max_ind[i]:
#         eval[i] = 1
# eval = eval.cpu().numpy()
# print(100 * eval.mean())



# ####### Model 2 GT 2
# _, sp_op_max_ind = torch.topk(sp_op, 4)
# _, sp_gt_max_ind = torch.topk(sp_gt,4)
# sp_op_max_ind = sp_op_max_ind.cpu().numpy()
# sp_gt_max_ind = sp_gt_max_ind.cpu().numpy()
# eval = np.zeros(len(sp_op_max_ind))
# for i in range(len(sp_op_max_ind)):
#     eval[i] = len(set(sp_op_max_ind[i]).intersection(set(sp_gt_max_ind[i])))
# print(25 * eval.mean())

###### Model 1 GT 2
# sp_op_max_ind = torch.argmax(sp_op, dim=1)
# _, sp_gt_max_ind = torch.topk(sp_gt, 2)
# eval = torch.zeros(len(sp_gt_max_ind))
# for i in range(len(sp_gt_max_ind)):
#     if sp_op_max_ind[i] in sp_gt_max_ind[i]:
#         eval[i] = 1
# eval = eval.cpu().numpy()
# print(100 * eval.mean())