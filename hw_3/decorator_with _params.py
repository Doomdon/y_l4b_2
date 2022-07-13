# t = start_sleep_time * 2^(n)
#
# if t < border_sleep_time
#     t = border_sleep_time if t >= border_sleep_time
import time


def decorator_with_params(call_count, start_sleep_time, factor, border_sleep_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Кол-во запусков = " + str(call_count) + "\nНачало работы")
            time1 = start_sleep_time
            i = 1
            while time1 <= border_sleep_time and call_count >= i:


                if time1 < border_sleep_time:
                    time1 = factor ** (i-1)
                elif time1 > border_sleep_time:
                    time1 = time1


                def result():
                    if time1 in [2, 3, 4]:
                        print("Запуск номер " + str(i) + ". Ожидание: " + str(time1) + " секунды. Результат "
                                                                                      "декорируемой функций = " +
                              str(func(*args, **kwargs)) + ". "
                              )
                    elif time1 in [1]:
                        print("Запуск номер " + str(i) + ". Ожидание: " + str(time1) + " секунда. Результат "
                                                                                      "декорируемой функций = " +
                              str(func(*args, **kwargs)) + ". "
                              )
                    else:
                        print("Запуск номер " + str(i) + ". Ожидание: " + str(time1) + " секунд.  Результат "
                                                                                      "декорируемой функций = " +
                              str(func(*args, **kwargs)) + ". "
                              )

                time.sleep(time1)
                result()
                i += 1

            print("Конец работы")

        return wrapper

    return decorator


@decorator_with_params(call_count=5, start_sleep_time=1, factor=2, border_sleep_time=10)
def func_multip(n):
    return n * 2


# тесты

if __name__ == "__main__":
    try:

        func_multip(2)
        func_multip(4)
        func_multip(3)
        func_multip(1)

    except KeyboardInterrupt:
        print('\nBye-bye')
