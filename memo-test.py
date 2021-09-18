import sys
import argparse

def main():
    parser = argpaarse.ArgumentParser()
    parser.add_argument('shelve')

    subparsers = parser.add_subparsers()
    add_parser = subparsers.add_parser('add')
    add_parser.set_defaults(func=cmd_add)
    list_parser.add_argument('-a', '--all', action="store_true")
    list_parser.set_defaults(func=cmd_list) 
    finish_parser = subparsers.add_parser('finish')
    finish_parser.add_argument('task')
    finish_parser.set_defaults('func=cmd_finish')

    args = paser.parse_args()

    db = shelve.open(args.shelve, 'c')
    try:
        args.db = db
        if hasattr(args, "func"):
            args.func(args)
        else:
            parser.print_help()
    finally:
        db.close()

def cmd_add(args):
    name = input('task name:')
    due_date = datetime.stptime(input('due date [y-m-d]:'), '%Y-%m-%d')
    required_time = int(input('required_time'))

    task = create_task(name, due_date, required_time)
    add_task(args.db, task)

def cmd_list(args):
    if args.all:
        tasks =all_task(args.db)
    else:
        task = unfinished_tasks(args.db)

    for key, task in tasks:
        print("{0} {1}".format(key, format_task(task)))

def cmd_finish(args):
    task = args.db[args.task]
    finish-task(task)
    args.db[args.task] = task

if __name__ == '__main__':
    main()

