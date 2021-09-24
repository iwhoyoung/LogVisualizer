import logging
import os
import time
import matplotlib.pyplot as plt


class Visualizer:
    """
    A tool to visualize training progress
    Usage:
        logger = visualizer.Visualizer(['train loss', 'ssim', 'Qabf'], ['r-o', 'b-o', 'y-o'], './log.txt')
        ...training code...
        logger.write_log([loss, ssim, qabf])
        logger.plot_loss()
    """

    def __init__(self, line_name: list, cut_num: int, line_color: list = None, log_path: str = None, is_log=False, name="log"):
        """
        :param pattern: name of loss
        :param log_path: log file name and path
        :param line_color: param to set line type when drawing, len(line_color) should be larger than len(pattern)
        """
        # assert len(pattern) <= len(line_color), 'line_color should contains more elements'
        self.name = name
        self.line_name = line_name
        self.cut_num = cut_num
        self.log_path = log_path
        self.line_color = line_color
        self.loss_curve = []
        if is_log:
            self.init_logger()
        # plt.ion()
        self.fig, self.ax_1 = plt.subplots()
        if cut_num != len(line_name):
            self.ax_2 = self.ax_1.twinx()
        pass

    def init_logger(self):
        if self.log_path is None:
            return
        logging.basicConfig(filename=os.path.join(self.log_path, self.name+'.log'), level=logging.DEBUG,
                            format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        logging.info('---LOG START---\n')
        # f = open(self.log_path + self.name +".txt", 'a+')
        # f.write('---LOG AT %s---\n' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        # f.close()

    def record(self, loss: list):
        """
        Pass in loss data which needs to be manipulated.
        :param loss: the loss data which needs to be manipulated and it has to be list.
        :return:none
        """
        self.loss_curve.append(loss)

    def log(self):
        """
        print the current loss.
        :return: none
        """
        loss = self.loss_curve[-1]
        log_item = [self.line_name[i] + ': %.4f, ' % loss[i] for i in range(0, len(loss))]
        print('epoch: %03d, ' % len(self.loss_curve) + ''.join(log_item))
        pass

    def write_log(self):
        """
        write the current loss into file.
        :return: none
        """
        if self.log_path is None:
            return
        loss = self.loss_curve[-1]
        log_item = [self.line_name[i] + ': %.4f, ' % loss[i] for i in range(0, len(loss))]
        logging.info('epoch: %03d, ' % len(self.loss_curve) + ''.join(log_item) + '\n')
        # f = open(self.log_path + self.name +".txt", 'a+')
        # f.write('epoch: %03d, ' % len(self.loss_curve) + ''.join(log_item) + '\n')
        # f.close()

    def write_other_log(self, content: str):
        """
        write the other info you want to write into file.
        :param content: the content you want to write into file.
        :return:none
        """
        if self.log_path is None:
            return
        logging.info(content + '\n')

    def plot_loss(self, is_show=False):
        """
        save the figure.
        :param is_show: whether show the figure or not.
        :return:none.
        """
        plt.cla()
        lines = []
        label = ['', '']
        for idx, curve_name in enumerate(self.line_name):
            loss = [item[idx] for item in self.loss_curve]
            if idx < self.cut_num:
                if self.line_color is None:
                    line, = self.ax_1.plot(list(range(1, len(loss) + 1)), loss)
                else:
                    line, = self.ax_1.plot(list(range(1, len(loss) + 1)), loss, self.line_color[idx])
                label[0] = label[0] + curve_name + ' / '
            else:
                if self.line_color is None:
                    line, = self.ax_2.plot(list(range(1, len(loss) + 1)), loss)
                else:
                    line, = self.ax_2.plot(list(range(1, len(loss) + 1)), loss, self.line_color[idx])
                label[1] = label[1] + curve_name + ' / '
            lines.append(line)
        plt.legend(lines, self.line_name)
        plt.xlabel('Epoch')
        self.ax_1.set_ylabel(label[0][0: -2])
        if self.cut_num != len(self.line_name):
            self.ax_2.set_ylabel(label[1][0: -2])
        plt.draw()
        plt.savefig(self.log_path + self.name + '.png')
        if is_show:
            plt.show()


# demo
if __name__ == '__main__':
    import random

    # generate a visualizer
    logger = Visualizer(['train loss', 'ssim', 'Qabf'], 3, log_path='./',name="log")
    # during training
    for i in range(0, 300):
        loss = 10 - i + random.random()
        ssim = (i + random.random()) / 10
        qabf = (i + random.random()) / 10
        logger.record([loss, ssim, qabf])
        # plot and write log
        logger.log()
        # logger.write_log()
    logger.plot_loss()

