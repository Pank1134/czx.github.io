import curses
import time


def display_letter_by_letter(stdscr, text, delay=0.05):
    """
    逐字显示文本内容
    :param stdscr: curses 窗口对象
    :param text: 要显示的文本
    :param delay: 每个字符显示的延迟时间
    """
    stdscr.clear()  # 清屏
    stdscr.refresh()
    row = 0  # 当前行
    for char in text:
        if char == '\n':  # 如果是换行符，移动到下一行
            row += 1
            stdscr.move(row, 0)
        else:
            stdscr.addch(char)  # 逐字显示
        stdscr.refresh()
        time.sleep(delay)  # 控制显示速度


def main(stdscr):
    # 初始化 curses 环境
    curses.curs_set(0)  # 隐藏光标
    stdscr.clear()

    # 信件内容
    letter = """
亲爱的妈妈：

您好！今天我想写一封信给您，表达我对您的感激之情。

妈妈，您每天都很辛苦，早上早早起床给我做早餐，送我上学，晚上还要帮我检查作业。我知道您为了我付出了很多，有时候我调皮惹您生气，但您总是耐心地教导我，从来没有放弃过我。谢谢您一直以来的关心和爱护。

记得有一次我生病了，您整夜都没睡，一直守在我床边，给我喂药、量体温。那时候我虽然很难受，但看到您那么担心我，我心里特别温暖。妈妈，您就像我的守护天使，总是在我最需要的时候陪在我身边。

还有，您总是鼓励我，让我勇敢面对困难。每当我遇到不会做的题目时，您总是耐心地教我，直到我明白为止。您让我知道，只要努力，就没有什么做不到的事情。

妈妈，我爱您！我会好好学习，听您的话，做一个懂事的孩子，不辜负您的期望。希望您每天都开开心心，不要太累了。

祝您身体健康，天天快乐！

您的孩子  
小明  
2023年10月
"""

    # 逐字显示信件内容
    display_letter_by_letter(stdscr, letter, delay=0.05)  # delay控制显示速度

    # 等待用户按任意键退出
    stdscr.getch()


# 运行程序
if __name__ == "__main__":
    curses.wrapper(main)