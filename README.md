# Automation of the enrollment process in courses

This project is a web-based application designed to automate the enrollment process for the University of Havana's Distance Education (EaD) and Course by Encounters (CPE) programs. The system streamlines applicant registration and provides administrative tools for managing entrance exams and generating specific reports.

## Introduction

With the recent changes in the study modalities at the University of Havana, there has been a significant increase in applicants for the EaD and CPE programs, surpassing 3,000 in recent years. Managing enrollment and entrance exams manually has become complex and poses challenges for staff performance and security. This system aims to:

- Simplify the applicant registration process.
- Manage entrance exams efficiently.
- Generate specific reports to aid administrative decision-making.

- ## Features

- **Applicant Registration**: Allows prospective students to register for courses online.
- **Entrance Exam Management**: Facilitates scheduling and administration of entrance exams.
- **Reporting**: Generates detailed reports on applicant data and enrollment statistics.
- **User Authentication**: Secure login for administrators to manage the system.

## The System

The system offers the possibility of being able to create a registration request, which will collect the data of the applicants, including the approval of the Affidavit. This form can be filled out by the applicant from outside the center, prepared from the center itself or by authorized personnel at the UH, in the presence of the applicant.

The preparation of this registration has a period that must be established by those responsible for this activity and taking into account the date on which each of the applications is made, it will serve to establish dates automatically. Applicants will go to the center to formalize their registration, choosing between the scheduled shifts or using the one assigned by the system.

At the time of registration validation, a classroom will be automatically assigned from those available for the applicant to take the exam. When the registrations have finished, the system will generate a document that will contain a list with the name of the applicants and the classroom where they will be examined.
Once the exams have been graded, the designated secretary must enter the grades into the system. At the required time, the races will be awarded automatically. With regard to the granting of majors, the students will be ordered by note and the majors will be distributed in order of priority. The races do not have a fixed number of places, that is, if two students have the same grade and are opting for a single place, the system will create two places.

At the end of the process, the system will also automatically generate three documents, a list that for each applicant will have the degree assigned. The second document will contain the closing note of the races whose places have been exhausted and the last document will have a list with information on all the remaining races.

## Technologies Used

- **Backend**: Python with Django framework
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript
- **Version Control**: Git

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:

```bash
git clone https://github.com/lorainemg/db-project.git
cd db-project
```
2. Create a Virtual Environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```
3. Install Dependencies:
```bash
pip install -r requirements.txt
```
4. Apply Migrations:
```bash
python manage.py migrate
```
5. Create a Superuser:
```bash
python manage.py createsuperuser
```
6. Run the Development Server:
```bash
python manage.py runserver
```

## Usage
- Applicant Registration: Applicants can sign up and apply for courses through the public interface.
- Administrator Access: Admins can log in to manage applicants, schedule exams, and generate reports.
