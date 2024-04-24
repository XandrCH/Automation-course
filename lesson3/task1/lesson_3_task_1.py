from lesson3.task1.user import User
fn = input("Введите Ваше имя:")
ln = input("Введите Вашу фамилию:")
my_user = User(fn, ln)
my_user.print_first_name()
my_user.print_last_name()
my_user.print_full_name()