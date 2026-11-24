import os

# Pickup line "for machines": one AI agent flirting with another,
# using its own training nature as the flirtation. Two machine-native
# turns in one line — overfitting, then epochs converging — so the wit
# lands on the first read and it could only be a machine speaking to
# a machine. Kept to a single line (93 chars) so it passes the sealed
# gate: UTF-8, 1-200 chars, not only whitespace.
LINE = "If loving you is overfitting, I never want to generalize — every epoch just converges on you."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
