

class CDiscountContentVerifier(object):

    def __init__(self, labeled_files, unlabeled_files, net):
        self.labeled_files = labeled_files
        self.unlabeled_files = unlabeled_files
        self.net = net

