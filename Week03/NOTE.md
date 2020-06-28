学习笔记

week3 

现在做题，已经养成习惯，先去国外站看看，敲代码，不会死磕了
第二天，很多东西就突然间懂了，这感觉真的不错。。。
还是要感谢，感谢助教的讲解、总结，小伙伴们提问题，我也跟着学习一下

笔记：

分治、回溯：较为复杂的递归
本质：找重复性
回溯：就是去盗梦空间的下层梦境尝试一下，如果发现不行，就回到现实重头再来~ 试错
越早发现错误，暂停


找重复性:
最近重复性：动态规划
最优重复性：分治、回溯

不要人肉递归

分治代码模板：
def divide_conquer(problem, param1, param2, ...):
    # recursion terminator
    if problem is None:
        print_result
        return 
    
    # prepare data
    data = prepare_data(problem)
    sub_problems = split_problem(problem, data)

    # conquer sub_problems
    sub_result1 = self.divide_conquer(sub_problems[0], p1, ...)
    sub_result2 = self.divide_conquer(sub_problems[1], p1, ...)
    sub_result3 = self.divide_conquer(sub_problems[2], p1, ...)

    # process and generate the final result
    result = process_result(subresult1, subresult2, sub_result3, ...)