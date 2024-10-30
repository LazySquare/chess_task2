# Шахматы в процедурном стиле
### Домашнее задание по программированию на Python.
Само задание выглядит так
```
Реализовать программу, которая позволяет играть в шахматы. Взаимодействие с программой происходит через консоль. Игровое поле изображается в виде восьми текстовых строк и дополнительных строк с буквенным обозначением столбцов. Программа должна предоставлять пользователю возможность поочередно вводить ходы за белых и черных.

  Программа проверяет корректность ввода - допускаются только ходы, соответствующие правилам шахмат. Например, для пешки нужно реализовать следующие правила:
a) Пешка может ходить вперёд на свободное поле, расположенное непосредственно перед ней на той же самой вертикали.
b) С исходной позиции пешка может продвинуться на два поля по той же самой вертикали, если оба эти поля не заняты.
c) Пешка ходит на поле, занимаемое фигурой или пешкой противника, которая расположена по диагонали на смежной вертикали, одновременно забирая эту фигуру или пешку.

Более сложные правила ходов для пешек (взятие на проходе и превращение в фигуру) реализовывать не нужно.

  Проверять наличие мата и шаха не надо. Программа должна считать количество сделанных ходов. В случае ошибки в ответ на ввод пользователя выводится сообщение вида: «Error. Type: ХХХ.». Должны поддерживаться следующие типы ошибок:
• Wrong input format. – Для неправильного формата ввода хода.
• The piece cannot make the specified move. – Выбранная фигура не может сделать указанный ход, первая позиция в нотации не содержит фигуру, или содержит вражескую фигуру.

Реализовать функцию подсказки выбора новой позиции фигуры: после выбора фигуры для хода функция подсказывает поля доступные для хода (формат ввода: координата и -) или фигуры соперника (с их позициями), доступные для взятия (формат ввода: координата), выбранной фигурой. Для короля этот функционал не обязателен.

Для подсказок полей доступных для хода и доступных для взятия вражеских фигур выводимые шахматные клетки необходимо отсортировать в алфавитном порядке (например "a6, b3, b5, d3, d5, e2, f1"). При попытке узнать возможные ходы фигуры противника - вывести сообщение как об отсутствии возможных ходов.
```



