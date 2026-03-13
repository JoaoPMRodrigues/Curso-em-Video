def maior(*n):
    m = -float("inf")
    for i in n:
        if i > m:
            m = i
    print(f"Foram informados {len(n)} valores.")
    print(f"O maior valor entre eles é: {m}")


maior(1, 2, 3, 5, 32, 543, 34, 54, 432, 423, 865, 264)
