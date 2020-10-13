import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Increase the verbosity", type=int)
ex_group=parser.add_mutually_exclusive_group()
ex_group.add_argument("-a", action="store_true")
ex_group.add_argument("-b", action="store_false")
parser.add_argument("num1", help="First number", type=int)
parser.add_argument("operation", help="Operation of the expression", type=str)
parser.add_argument("num2", help="Second number", type=int)
args=parser.parse_args()
result=0
if args.operation=="+":
    result=args.num1+args.num2
if args.operation=="-":
    result=args.num1-args.num2
if args.operation=="*":
    result=args.num1*args.num2
if args.operation=="/":
    result=args.num1/args.num2
if args.verbose==0:
    print(result)
elif args.verbose==1:
    print("The result of the expression is: {}".format(result))
else:
    print("The result of the expression {} {} {} is: {}".format(args.num1, args.operation, args.num2, result))

