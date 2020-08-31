from pylint.lint import Run

results = Run(['../src', "--rcfile=../.pylintrc", "--output-format=colorized"], do_exit=False)
if results.linter.stats['global_note'] < 9:
    exit(-1)