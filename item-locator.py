print("Item Locator")
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
position = input("where do you want to put the item? First type the column then type the row")
horizontal = int(position[0])
vertical = int (position[1])

selected_row = map[vertical -1]
selected_row[horizontal - 1] = 'X'
print(f"{row1}\n{row2}\n{row3}")
