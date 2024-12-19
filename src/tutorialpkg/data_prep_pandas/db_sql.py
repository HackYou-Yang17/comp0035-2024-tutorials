import pathlib
import pandas as pd
import sqlite3 as sql


def create_norm_table(df, db_path):

    conn = sql.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('PRAGMA foreign_keys = ON;')
    conn.commit()

    student_sql = '''CREATE TABLE student (
                                student_id INTEGER,
                                student_name STRING NOT NULL,
                                student_email STRING NOT NULL UNIQUE,
                                PRIMARY KEY (studentid));
                                '''
    
    teacher_sql = '''CREATE TABLE teacher (
                                teacher_id INTEGER,
                                teacher_name STRING NOT NULL,
                                teacher_email STRING NOT NULL,
                                PRIMARY KEY (teacher_id));
                                '''
    
    course_sql = '''CREATE TABLE course (
                                course_id INTEGER,
                                course_name STRING NOT NULL,
                                course_code INTEGER NOT NULL,
                                course_schedule STRING,
                                course_location STRING,
                                PRIMARY KEY (course_id));
                                '''

    enrollment_sql = '''CREATE TABLE enrollment (
                                student_id INTEGER NOT NULL, 
                                course_id INTEGER NOT NULL,
                                teacher_id INTEGER,
                                PRIMARY KEY (student_id, course_id, teacher_id),
                                FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
                                FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE ON UPDATE CASCADE,
                                FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id) ON UPDATE CASCADE ON DELETE SET NULL);
                                '''
    
    cursor.execute(student_sql)
    cursor.execute(teacher_sql)
    cursor.execute(course_sql)
    cursor.execute(enrollment_sql)

    conn.close()

def create_unnorm_table(df, db_path):

    conn = sql.connect(db_path)
    df.to_sql('enrollments', conn, if_exists='replace', index=False)
    conn.close()

if __name__ == '__main__':

    df_path = pathlib.Path(__file__).parent.parent.joinpath('data_db_activity', 'student_data.csv')
    db_path = pathlib.Path(__file__).parent.parent.joinpath('data_db_activity', 'enrollments_unnormalised.db')
    df = pd.read_csv(df_path)
    
    create_unnorm_table(df, db_path)

    
