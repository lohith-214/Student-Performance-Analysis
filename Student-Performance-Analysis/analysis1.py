import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """Load the student dataset."""
    return pd.read_csv(file_path)


def clean_data(df):
    """Handle missing values."""
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())

    df = df.fillna(0)

    print("\nMissing values after cleaning:")
    print(df.isnull().sum())
    return df


def explore_data(df):
    """Basic exploration of the dataset."""
    print("\nDataset Preview:")
    print(df.head())

    print("\nData Types:")
    print(df.dtypes)

    print("\nBasic Statistics:")
    print(df.describe())


def subject_analysis(df):
    """Analyze average marks by subject."""
    subjects_avg = df[["Math", "Science", "English"]].mean()
    print("\nAverage marks by subject:")
    print(subjects_avg)
    return subjects_avg


def attendance_analysis(df):
    """Analyze attendance vs performance."""
    attendance_math = df.groupby("Attendance")["Math"].mean()
    attendance_english = df.groupby("Attendance")["English"].mean()

    print("\nAttendance vs Math performance:")
    print(attendance_math)

    print("\nAttendance vs English performance:")
    print(attendance_english)

    return attendance_math, attendance_english


def plot_subject_averages(subjects_avg):
    """Bar chart for average marks."""
    subjects_avg.plot(kind="bar")
    plt.title("Average Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Marks")
    plt.tight_layout()
    plt.show()


def plot_attendance_vs_math(attendance_math):
    """Line chart for attendance vs math performance."""
    attendance_math.plot(marker="o")
    plt.title("Attendance vs Math Performance")
    plt.xlabel("Attendance Percentage")
    plt.ylabel("Average Math Score")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    data = load_data("students.csv")
    data = clean_data(data)

    explore_data(data)

    subjects_avg = subject_analysis(data)
    attendance_math, _ = attendance_analysis(data)

    plot_subject_averages(subjects_avg)
    plot_attendance_vs_math(attendance_math)


if __name__ == "__main__":
    main()
