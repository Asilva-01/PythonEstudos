def main():
    cond1 = True
    cond2 = True
    cond3 = True

    if cond1 and cond2 and cond3:
        print("Todas são verdadeiras")
    elif cond1 or cond2 or cond3:
        print("Pelo menos uma delas é verdadeiras")
    else:
        print("Ambas são falsas")
main()
