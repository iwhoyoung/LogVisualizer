# LogVisualizer

let log data to be visualized.

Help on module visualizer:

NAME
    visualizer

CLASSES
    builtins.object
        Visualizer

    class Visualizer(builtins.object)
     |  Visualizer(line_name: list, cut_num: int, line_color: list = None, log_path: str = None, is_log=False, name='log')
     |
     |  A tool to visualize training progress
     
Usage
===
     |      logger = visualizer.Visualizer(['train loss', 'ssim', 'Qabf'], ['r-o', 'b-o', 'y-o'], './log.txt')
     |      ...training code...
     |      logger.write_log([loss, ssim, qabf])
     |      logger.plot_loss()
     |
     |  Methods defined here:
     |
     |  __init__(self, line_name: list, cut_num: int, line_color: list = None, log_path: str = None, is_log=False, name='log')
     |      :param pattern: name of loss
     |      :param log_path: log file name and path
     |      :param line_color: param to set line type when drawing, len(line_color) should be larger than len(pattern)
     |
     |  init_logger(self)
     |
     |  log(self)
     |      print the current loss.
     |      :return: none
     |
     |  plot_loss(self, is_show=False)
     |      save the figure.
     |      :param is_show: whether show the figure or not.
     |      :return:none.
     |
     |  record(self, loss: list)
     |      Pass in loss data which needs to be manipulated.
     |      :param loss: the loss data which needs to be manipulated and it has to be list.
     |      :return:none
     |
     |  write_log(self)
     |      write the current loss into file.
     |      :return: none
     |
     |  write_other_log(self, content: str)
     |      write the other info you want to write into file.
     |      :param content: the content you want to write into file.
     |      :return:none


The .py file contains demo.
