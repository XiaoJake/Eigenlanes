import os
import torch

import numpy as np

class Config(object):
    def __init__(self):
        # --------basics-------- #
        self.setting_for_system()
        self.setting_for_path()
        self.setting_for_image_param()
        self.setting_for_dataloader()
        self.setting_for_visualization()
        self.setting_for_save()
        # --------preprocessing-------- #
        self.setting_for_lane_representation()
        # --------others-------- #
        self.setting_for_lane_detection()

    def setting_for_system(self):
        self.gpu_id = "1"
        self.seed = 123
        os.environ["CUDA_VISIBLE_DEVICES"] = self.gpu_id
        torch.backends.cudnn.deterministic = True

    def setting_for_path(self):
        self.pc = 'main'
        self.dir = dict()

        self.setting_for_dataset_path()  # dataset path

        self.dir['proj'] = os.path.dirname(os.getcwd()) + '/'
        self.dir['head_proj'] = '/'.join(self.dir['proj'].split('/')[:-2]) + '/'
        self.dir['pre0'] = self.dir['head_proj'] + 'P00_data_processing/output_{}/pickle/'.format(self.datalist)
        self.dir['out'] = os.getcwd().replace('code', 'output') + '_{}/'.format(self.datalist)

    def setting_for_dataset_path(self):
        self.dataset = 'tusimple'  # ['tusimple']
        self.datalist = 'train_set'  # ['train_set'] only

        # ------------------- need to modify -------------------
        self.dir['dataset'] = '--dataset_dir'
        # ------------------------------------------------------

    def setting_for_image_param(self):
        self.org_height = 720
        self.org_width = 1280
        self.height = 384
        self.width = 640
        self.size = [self.width, self.height, self.width, self.height]
        self.mean = [0.485, 0.456, 0.406]
        self.std = [0.229, 0.224, 0.225]
        self.crop_size = 180

    def setting_for_dataloader(self):
        self.num_workers = 4
        self.batch_size = 1
        self.data_flip = True

    def setting_for_visualization(self):
        self.display_all = True

    def setting_for_save(self):
        self.save_pickle = True

    def setting_for_lane_detection(self):
        self.max_lane_num = 5

    def setting_for_lane_representation(self):
        self.min_y_coord = 0
        self.max_y_coord = 330
        self.node_num = self.max_y_coord
        self.py_coord = self.height - np.float32(np.round(np.linspace(self.max_y_coord, self.min_y_coord + 1, self.node_num)))

        # threshold for excluding some lanes (too short or horizontal)
        self.thresd_theta = 1
        self.thresd_ratio_for_short_lane = 4

