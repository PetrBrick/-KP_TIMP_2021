def ask(number):
    questions = {10: 'определение булевой функции от n переменных',
                 11: 'теорему о числе булевых функций от n  переменных',
                 12: 'определение фиктивной переменной',
                 13: 'определение существенной переменной',
                 14: 'определение дизъюнктивной нормальной формы функции',
                 15: 'определение конъюнктивной нормальной формы функции',
                 16: 'определение полной системы булевых функций',
                 17: 'теорему о функциональной полноте системы булевых функций',
                 18: 'определение замыкания множества',
                 19: 'определение замкнутого множества',
                 20: 'определение функций, сохраняющих ноль',
                 21: 'определение функций, сохраняющих единицу',
                 22: 'определение самодвойственной функции',
                 23: 'определение линейной функции',
                 24: 'определение монотонной функции',
                 25: 'определение полной системы булевых функций',
                 26: 'лемму о несамодвойственной функции',
                 27: 'лемму о немонотонной функции',
                 28: 'лемму о нелинейной функции',
                 29: 'теорему Поста',
                 30: 'следствие теоремы Поста'}
    return questions[number]


def ans(number):
    answers = {
        10: 'Булевой функцией от n булевых переменных или n-местной булевой функцией называется отображение множества {0, 1} n-ой степени в множество {0, 1}.	 ',
        11: 'Число различных булевых функций от n переменных равно 2 в степени 2 встепени n.	 ',
        12: 'Переменная x называется фиктивной для функции f(x,...), если значение функции не зависит от значения переменных.	 ',
        13: 'Переменная x называется существенной для функции f(x,...), если значение функции зависит от значения переменных. 	 ',
        14: 'Дизъюнктивной нормальной формой (ДНФ) булевой функции f называется реализующая f формула, являющаяся дизъюнкцией элементарных конъюнкций. В отличии от СДНФ дизъюнктивная нормальная форма функции f определяется неоднозначно, т.е. f может иметь несколько реализующих ее ДНФ.	 ',
        15: 'Конъюнктивной нормальной формой (КНФ) булевой функции f называется реализующая f формула, являющаяся конъюнкцией элементарных дизъюнкций. Аналогично ДНФ, конъюнктивная нормальная форма функции f определяется неоднозначно, т.е. f может иметь несколько реализующих ее КНФ.	 ',
        16: 'Система (множество) булевых функций называется функционально полной, если любая булева функция может быть выражена в виде формулы над B.	 ',
        17: 'Пусть F={f1, f2,...} и G={g1, g2,...} - системы булевых функций, при этом F - функционально полная система и каждая ее функция может быть выражена формулой в базисе G. Тогда G - функционально полная система.	 ',
        18: 'Замыканием множества М называется множество всех функций, которые можно реализовать формулами в базисе М.	 ',
        19: 'Множество называется замкнутым множеством, если оно совпадает со своим замыканием.	 ',
        20: 'Функцией, сохраняющей ноль (Т0), называется функция, которая на наборе из всех нулей будет равна 0. f(0,...) = 0	 ',
        21: 'Функцией, сохраняющей единицу (Т1), называется функция, которая на наборе из всех единиц будет равна 1. f(1,...) = 1	 ',
        22: 'Самодвойственная функция (S) — булева функция, двойственная сама к себе, другими словами самодвойственная функция на противоположных друг другу наборах значений аргументов принимает противоположные значения.	 ',
        23: 'Функция называется линейной (L), если каждое элементарное произведение канонического полинома Жегалкина, который представляет эту функцию, имеет не больше одного сомножителя.	 ',
        24: 'Булева функция называется монотонной, если из того, что она принимает значение 1 на некотором наборе аргументов А, следует, что она принимает значение 1 на всяком наборе аргументов B, который получается из набора аргументов A путём замены произвольного числа нулей на единицы.	 ',
        25: 'Система (множество) булевых функций В называется функционально полной, если любая булева функция может быть выражена в виде формулы над B.	 ',
        26: 'Если функция f не принадлежит классу самодвойственных функций, то подставляя в функцию вместо переменных x и не x, можно получить функцию, равную константе (1, 0).	 ',
        27: 'Если функция f не принадлежит классу монотонных функций, то подставляя в функцию вместо переменных 1 и 0, можно получить функцию, равную не x.	 ',
        28: 'Если фуекция f не принадлежит классу линейных, то в АНФ функции f найдется хотя бы одно слагаемое, содержащее произведение каких-то двух переменных.	 ',
        29: 'Для того, чтобы система функций В была функционально полной необходимо и достаточно, чтобы она целиком не лежала ни в одном из 5 основных замкнутых классов: T0 T1 S M L.	 ',
        30: 'Всякий отличный от Р2 замкнутый класс булевых функций целиком содержится по крайней мере в одном из 5 замкнутых классов: T0 T1 S M L.	 '}
    return answers[number]

def clas(input):
    types = {
        1: "T0",
        2: "T1",
        3: "S",
        4: "M",
        5: "L"
    }
    return types[input]