#login system
#massive project number 1
print('Welcome to account registration and Login.')
option = input('Do you wanna sing up or log in ?(L/S) : ')
if option.upper() == 'S':
        user_name = input('Enter your user_name : ')
        password = input('Set your password : ')
        forgot_pass_ques = input('Enter your favourite question(name/school/food/place) : ')
        forgot_pass_ques_ans = input('Enter your question"s answer : ')
        with open('data.txt','w') as file:
            file.write(f'user_name={user_name}\n')
            file.write(f'password={password}\n')
            file.write(f'forgot_question={forgot_pass_ques}\n')
            file.write(f'forgot_question_answer={forgot_pass_ques_ans}\n')
        print('New user Registered successfully!')
        option = input('Do you wanna signup or log in (L/S) : ')
if option.upper() == 'L':
    username = input('Enter your username : ')
    passw= input('Enter your password (f) for forgot pass: ')
    with open('data.txt','r') as file:
        #returns a list
        try :
                login_creds = file.readlines()
                login_cred_username = login_creds[0].split('=')
                login_cred_pass = login_creds[1].split('=')
                login_cred_forgot_question = login_creds[2].split('=')
                login_cred_forgot_question_answer = login_creds[3].split('=')

                if passw == 'f':
                    ques = input(f'Whta is your favourite {login_cred_forgot_question[1][:-1]}? :')
                    if ques == login_cred_forgot_question_answer[1][:-1]:
                        print(f'your old password was {login_cred_pass[1][:-1]}')
                        change = input('Do you wanna reset your password ? (y/n)')
                        if change.lower() == 'y':
                            a_file = open('data.txt','r')
                            new_pass = input('enter your new password : ')
                            lines = r_file.readlines()
                            a_file = open('data.txt','w')
                            lines[1] = f'password={new_pass}\n'
                            a_file.writelines(lines)
                            a_file.close()
                            # w_file.close()
                elif username != login_cred_username[1][:-1] or passw != login_cred_pass[1][: -1]:
                    print('Wrong credentials.')
                else:
                   print('Logged in successfully!')
        except IndexError:
                    print('Register for an account first!')
