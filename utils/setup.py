import torch
import random
import numpy as np
import logging
from configs.msnet import msnet_config
from configs.msknet import msknet_config
from configs.mfnet import mfnet_config
from configs.st_gcn import st_gcn_config
from configs.sgn import sgn_config
def setup_device(args):
    if torch.has_cuda:
        args.device = 'cuda'
        logging.info('Model running on cuda.')
    else:
        args.device = 'cpu'
        logging.info('Model running on cpu.')
    args.n_gpu = torch.cuda.device_count()


def setup_seed(args):
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)


def setup_logging():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    return logger

def setup(args_parser,args):

    setup_logging()
    if args.model_name == 'msnet':
        args = msnet_config(args_parser)
    elif args.model_name == 'msknet':
        args = msknet_config(args_parser)
    elif args.model_name == 'mfnet':
        args = mfnet_config(args_parser)
    elif args.model_name == 'st-gcn':
        args = st_gcn_config(args_parser)
    elif args.model_name == 'smlp':
        args = st_gcn_config(args_parser)
    elif args.model_name =='sgn':
        args = sgn_config(args_parser)

    args = args.parse_args(args = [])
    setup_device(args)
    setup_seed(args)
    return args