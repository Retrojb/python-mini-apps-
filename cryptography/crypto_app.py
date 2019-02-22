from tkinter import Tk, messagebox, simpledialog

def get_task():
    task = simpledialog.askstring('Task', 'Good Day 007: \n Would you like to send or read a secret message to M? '
                                          '\n Want to Encrypt or Decrypt?')
    return task


def get_message():
    message = simpledialog.askstring('Message', 'Enter your message')
    return message


def is_even(number):
    return number % 2 == 0


def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters


def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters


def letter_swap(message):
    letter_list = []
    if not is_even(len(message)):
        message = message = 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message


def encrypt(message):
    message_swap = letter_swap(message)
    encrypted_message = ''.join(reversed(message_swap))
    return encrypted_message


def decrypt(message):
    unreversed_message = ''.join(reversed(message))
    decrypted_message = letter_swap(unreversed_message)
    return decrypted_message


def close_app():
    root.destroy()


root = Tk()
root.resizable(0, 0)
root.withdraw()


while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        encrypted = letter_swap(message)
        messagebox.showinfo('Ah Mr Bond: The decrypted message from M is:', encrypted)
    elif task == 'decrypt':
        message = get_message()
        decrypted = letter_swap(message)
        messagebox.showinfo('Good Day 007, send M an encrypted message', decrypted)
    else:
        error = 'You must have done something wrong please enter: encrypt or decrypt?'
        messagebox.showinfo('Message Error', error)



root.mainloop()