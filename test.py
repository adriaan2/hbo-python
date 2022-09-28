from pickle import TRUE


more_letters = input("More Letters? (Yes or No)")
if "No" in more_letters:
    print("okay bye.")
elif "Yes" in more_letters:
    type_letter = input("Job Offer or Rejection?")
check=False    
def job():
    first_name = input("First Name?").capitalize()
    first_length = len(first_name)
    if first_length >= 2 and first_length < 11:
        last_name = input("Last Name?").capitalize()
        last_length = len((last_name))
        if last_length >= 2 and last_length < 11:
            while check==True:
              jobtitle=input("cdergvyt")
              joblen=len(jobtitle) 
              if joblen>=10:
                    check==False 
                    annual_salary = input("Annual Salary?")
                    start_date = input("Start Date?(YYYY-MM-DD)")
    print("Dear", first_name, last_name,",")
    print("After careful evaluation of your application for the position of",jobtitle, "we are glad to offer you the job. Your salary will be", annual_salary,"euro annually.")
    print("Your start date will be", start_date,". Please do not hesitate to contact us with any questions.")
    print("Sincerely,")
    print("HR Department of XYZ")
job()