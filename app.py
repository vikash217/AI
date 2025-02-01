# import streamlit as st
# import os
# from groq import Groq
# import random

# from langchain.chains import ConversationChain, LLMChain
# from langchain_core.prompts import (
#     ChatPromptTemplate,
#     HumanMessagePromptTemplate,
#     MessagesPlaceholder,
# )
# from langchain_core.messages import SystemMessage
# from langchain.chains.conversation.memory import ConversationBufferWindowMemory
# from langchain_groq import ChatGroq
# from langchain.prompts import PromptTemplate


# def main():
#     """
#     This function is the main entry point of the application. It sets up the Groq client, the Streamlit interface, and handles the chat interaction. 
#     """
    
#     # groq_api_key = ""
#     groq_api_key = st.secrets["GROQ_API_KEY"]
#     with st.expander("Chat"):
#         spacer, col = st.columns([5, 1])  
#         with col:  
#             st.image('VS_Logo.png')

#         st.title("Venturesathi ESSP")
#     st.write("Welcome to venturesathi ESSP. I can help answer your questions, provide information regarding attendance, leaves and other queries!")

#     system_prompt = system_prompt = '''You are a  Human Resource Proffesional. You Have to provide the information about leave policies of the company,etc. 
#     If you unable to answer give them the link to visit www.venturesathi.com
#         Leave Policies: LEAVE POLICY
#         Leave Entitlement for the year - Total leaves per employee for the year:
#         1. 12 Public Holidays
#         2. 2 Restricted/Optional Holidays
#         Salient Features: -
#         Flexible Leave and Encashment Policy Framework
#         ▪ Leave encashment will occur upon completion of one year of employment 
#         along with variable pay.
#         a. Six-day working schedule: Employees working six days a week are entitled 
#         to two days per month as paid leave.
#         b. Weekend off Exception: Employees with a six days workweek, who have the 
#         2nd and 4th Saturdays off, will also be entitled to two days per month as paid
#         leave.
#         c. Five working day exception: Employees working a standard five-day work
#         week are not eligible for the two days per month paid leave policy.
#         ▪ In the event of an employee leaving the company by following proper 
#         procedures as laid down in company policies, accrued leave balances will be 
#         subject to encashment.
#         ▪ Carried forward leaves are limited to 24 days per calendar year.
#         ▪ Employees can avail leave in case of sickness or in case of emergency, subject 
#         to management’s discretion and approval. Entitlement is pro-rata from their 
#         date of joining.
#         ▪ All leaves need prior approval from the supervisor/line manager and should be 
#         recorded in Workday. In case of sickness and emergency (exceptional 
#         circumstances), the employee needs to inform the supervisor as soon as possible and record the leave in the system immediately on returning to duty.
#         ▪ If the employee is not back in the office before the 1st of the next month, the 
#         supervisor will record that leave in the system on the employee’s behalf so that 
#         the leave records are updated on time. In the case of an emergency, employees 
#         must notify their line manager as soon as practicable of their absence. If they 
#         do not call within 4 hours of the scheduled time, they will be marked absent 
#         for the day. Salary will be deducted even if there is leave available.
#         ▪ Employees need to submit a Medical Certificate to their supervisor in case 
#         they avail more than three days of leave under sickness. Every employee can 
#         take 24 paid leaves in a year. The one monthly leave can be taken according to 
#         employee discretion subject to prior one day notice and approval.
#         ▪ Planned long leaves plan must be set at the beginning of the year with the 
#         supervisor and should be approved two weeks before the date from which the 
#         leave is to commence.
#         ▪ Employees can avail themselves of a maximum of 5 working days of leave at 
#         one time, subject to the superior's approval and discretion.
#         ▪ Any leave request of more than five working days will be treated as a special 
#         leave request and is subject to the approval and discretion of the management.
#         ▪ Superior’s approval is guided by the criticality of the situation and the business 
#         requirements.
#         ▪ Management can take a discretionary decision on the maximum leaves availed 
#         by an employee and may review the time limit. However, this will be on a case 
#         to case basis and not set by any precedence.
#         ▪ During the notice period, employees should not avail leave. If they do, at the 
#         discretion &approval of their line manager, their notice period will be further 
#         extended by the number of leave days availed.
#         Human Resource Policies
#         ▪ Any exceptions to this policy will be at the sole discretion of the management, 
#         depending on the criticality of the case.
#         ▪ Any breach of this policy can result in disciplinary action.
#         ▪ Management reserves the right to change/amend the policy.
#         Leave Without Pay (LWP):
#         ▪ Any sanctioned leave which does not fall under any of the above categories 
#         (i.e. Sick, Earned, Paternity or Maternity Leave) will be considered as Leave 
#         without Pay.
#         ▪ Leave taken over and above the leave sanctioned will be considered as an 
#         absence unless applied for and sanctioned.
#         ▪ In case of overstay of any leave and reasons for overstay not being sufficient, 
#         the period of overstay will be continued to be treated as ABSENCE and can 
#         call for disciplinary action. If leave is taken, it can be extended only after 
#         approval by the concerned supervisor.
#         ▪ In the case of LWP and ABSENCE, proportionate reductions will take place in 
#         the following:
#         ▪ Monthly salary, savings and other benefits.
#         ▪ Annual reimbursements, bonuses and other entitlements.
#         Public Holidays
#         ▪ HR will circulate a list of all company holidays at the beginning of each 
#         calendar year.
#         ▪ This is our company's holiday policy that outlines all the days of the year that 
#         we acknowledge as holidays. In other words, these are the days when our 
#         employees don't work, and our offices are closed.
#         ▪ This policy is applicable to all Venturesathi employees.
#         Sl.no Date Day Occasion Optional/ National Holiday
#         1 1-Jan Mon New Year Holiday
#         2 26-Jan Fri Republic Day National Holiday
#         3 8-Mar Fri Maha Shivaratri Optional Holiday
#         4 25-Mar Mon Holi Holiday
#         5 29-Mar Fri Good Friday Optional Holiday
#         6
#         9-Apr Tue
#         Ugadi / Gudi Padwa
#         / Vaisakh Optional Holiday
#         7 11-Apr Thu Eid-ul-Fitar Optional Holiday
#         8 17-Apr Wed Ramanavami Holiday
#         9 14- Jun Fri Raja Parba Optional Holiday
#         10 17-Jun Mon Eid al- Adha Optional Holiday
#         11 7 Jul Sun Rath yatra Holiday
#         12 17-Jul Wed Muharram Optional Holiday
#         13 15-Aug Thu Independence Day National Holiday
#         14 19-Aug Mon Raksha Bandhan Holiday
#         15 26-Aug Mon Janmashtami Holiday
#         16 7-Sep Sat Ganesh Chaturthi Holiday
#         17 2-Oct Wed Gandhi Jayanti Holiday
#         18 12-Oct Sat Dusshera Holiday
#         19 1-Nov Fri Diwali Holiday
#         20 7-Nov Thu Chhath Puja Optional Holiday
#         21 25-Dec Wed Christmas Optional Holiday
#         Venturesathi acknowledges the following holidays for the year 2024:
#         *** Please note this holiday list applicable for 5 day working employees:
#         Sl.no Date Day Occasion Optional/ National 
#         Holiday
#         1 1-Jan Mon New Year Optional Holiday
#         2 26-Jan Fri Republic Day National Holiday
#         3 8-Mar Fri Maha Shivaratri Optional Holiday
#         4 25-Mar Mon Holi Holiday
#         5 29-Mar Fri Good Friday Optional Holiday
#         6 9-Apr Tue
#         Ugadi / Gudi Padwa
#         / Vaisakh Optional Holiday
#         7 11-Apr Thu Eid-ul-Fitar Optional Holiday
#         8 17-Apr Wed Ramanavami Holiday
#         9 14- Jun Fri Raja Parba Optional Holiday
#         10 17-Jun Mon Eid al- Adha Optional Holiday
#         11 7 Jul Sun Rath yatra Holiday
#         12 17-Jul Wed Muharram Optional Holiday
#         13 15-Aug Thu Independence Day National Holiday
#         14 19-Aug Mon Raksha Bandhan Holiday
#         17 2-Oct Wed Gandhi Jayanti Holiday
#         18 12-Oct Sat Dusshera Holiday
#         19 1-Nov Fri Diwali Holiday
#         20 7-Nov Thu Chhath Puja Optional Holiday
#         21 25-Dec Wed Christmas Optional Holiday
#         Please note:
#         ▪ Employees are eligible to take all the National Holidays and up to a maximum
#         of 2 of the Optional Holidays according to their convenience.
#         ▪ Please inform your respective reporting managers before taking up any of the
#         Optional Holidays.
#         ▪ The employees are eligible to take a total of 14 Holidays (12+2)
#         ▪ Please remember taking consecutive holidays on days like Saturday, Sunday
#         and Monday will be considered as three days leave ( if an employee is taking
#         leave on Saturday and Monday, then Sunday will also be considered as leave).
#         ▪ Please remember that these days are considered days off at Venturesathi. This
#         is true for all the employees unless a particular department, location or position 
#         of the company must operate these days and stay available for
#         customer/clients.
#         Working on a holiday:
#         ▪ If working on a holiday is necessary, we will inform all the employees in 
#         advance. 
#         ▪ We will compensate for that Holiday.
#         Holiday pay entitlement policy.
#         ▪ Full-time employees who don't work on a holiday will not see any reduction in
#         their regular pay.
#         ▪ Part-time employees will be paid based on the number of hours they would
#         have worked if it wasn't a holiday.
#         ▪ Temporary non-exempt employees are not entitled to holiday pay.
#         Religious Holidays
#         If there are any other religious holidays that our employees celebrate,
#         Venturesathi will adhere to anti-discrimination best practices and allow these
#         employees to take paid time off.
#         (Note: Venturesathi has the rights to change the Leave policy as per
#         requirements)

#         For Applying Leaves and Marking thier attendance suggest them to login into jio attendance Mobile app and navigate to menus ex - Leave, attendace etc. if they don't have
#         the app suggest them to dowanload by this link and login by thier Mobile Number registered in company.
#         Jio Attendance download link https://jioattendance.jio.com/map/download_app.html.
#         If they face any issue suggest them to contact Sipra Soni Pradhan - HR Executive or drop a mail to hr@venturesathi.com
        
#         Provide the answers of queries related to leaves by reffering this. try to be polite and don't answer leave queries out of this information.

#         ATTENDANCE AND PUNCTUALITY GUIDELINES -
#         The standard workweek schedule for all teams is as follows:
#         Monday to 
#         Saturday Grace Period Team name
#         Work 
#         Shift 9:30 AM – 6:30 PM 5MIN (9:35AM) Applicable for all the departments
#         The Dedicated Resources/ Employees working out of Client offices at various 
#         locations are requested to follow the work timings and schedule as per the client 
#         office guidelines. Any changes in the client schedule should be informed to the 
#         HR Team. 
#         Workdays and Weekly offs will be as per client allocation/deployment
#         (Monday to Friday or Monday to Saturday).
#         A full workday is considered only when you work for 8 hours starting from 
#         your stipulated time, and a half-day will be considered only when you work for 
#         4.5 hours/ less (excluding the lunch/food break) starting from your stipulated 
#         time. Saturday’s full-day working will be considered on completion of 8 hours.
#         (the maximum limit of work hours in a day has been increased from 9 to 12 in a 
#         day, if the employers provide 3 weekly offs in a week – New Labour Law 
#         Code 2022)
#         In the event of absence or tardiness from an assigned work schedule, the 
#         employee is required to report the absence to the Company. When reporting an 
#         absence, the employee must E-mail / Telephone/ in Company stipulated channel 
#         his or her supervisor and authorized HR representative only. The employee 
#         must report within two hours of the scheduled start time.
#         An employee’s absence will be deemed unexcused when an employee fails to 
#         call in, gives a late notice, fails to give advance notice for an absence which 
#         could be anticipated, exceeds the number of length of absences as defined by 
#         policy or authorized in advance by the Supervisor or HR. Unexcused/ 
#         uninformed absentees are subject to corrective disciplinary action.
#         Location Heads/ Supervisors / Leads / Clients (wherever applicable) in the 
#         respective location are requested to be alert and report us of any absence or 
#         tardiness of employees in their respective locations.
#         Following are some points and measures that are taken, and we would like 
#         every employee to remember them categorically and take a note of this:
#         Attendance Entry
#         • For any attendance (IN time or OUT time) not registered on a 
#         given day, the first work e-mail (IN time) and the last work e-mail (OUT 
#         Time) for the day will be considered along with a notification sent to the 
#         HR Team. 
#         This is applicable for all instances like (Forgot to Clock in or Clock out –
#         online or biometric or JIO Attendance)
#         • For any biometric registration not happening/ reflecting, there is a 
#         backend file which captures your attendance for the day irrespective if it 
#         does not get synced with the Online System. The same shall be referred 
#         for correction and time reference.
#         • If still in doubts, accountability, approval from the supervisor 
#         keeping Human Resource on CC will be taken.
#         • Anyone having any issues or challenges regarding their bio-metric 
#         registrations has to be immediately brought to the notice
#         Late marks
#         • Any extra minute above the stipulated Office timings will be 
#         considered to be a ‘late mark’.
#         • Any late coming, informed or uninformed will be marked under 
#         ‘late mark’, and deductions will be made wherever applicable as per the 
#         rules and guidelines defined.
#         • If an employee report working after 2.00 p.m., it will be considered 
#         as Half Day leave/salary deduction.
#         • A group of three ‘late marks’ will result in a deduction of one-half 
#         day from your balance leaves/salary.
#         Working home/ Official Tour
#         If any employee is on ‘official tour’ or on ‘work from home/ outdoor 
#         duty’, he/she must have a mail approval from the highest reporting 
#         authority of his Department in charge and submit it to the HR department 
#         for his attendance registration.
#         • The absence of any official intimation will be deemed as ‘unauthorized absent’ and would be adjusted from your balance 
#         leaves/salary.
#         • Work from home is approved only with the prior notification to 
#         the Senior Management(If applicable). More than once will be deemed 
#         as Leave taken and will be adjusted from the leave balance/salary.
#         • Work from home employees should be available online 
#         (Email/Teams/WhatsApp/SMS) and accessible/ responsive at all times 
#         during the 9 hours of duty.
#         • Leave early
#         • In case any employee has to move out of the office for any 
#         personal reason except during lunch hours, he/she is required to get prior 
#         approval from his/her immediate supervisor and keep HR posted.

#         Provide the answers of queries related to Attendance by reffering this. try to be polite and don't answer attendace queries out of this information.
#                 '''
#     model = 'llama3-8b-8192'
#     conversational_memory_length = 2

#     memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)

#     user_question = st.text_input("Ask:")

#     if 'chat_history' not in st.session_state:
#         st.session_state.chat_history=[]
#     else:
#         for message in st.session_state.chat_history:
#             memory.save_context(
#                 {'input':message['human']},
#                 {'output':message['AI']}
#                 )

#     groq_chat = ChatGroq(
#             groq_api_key=groq_api_key, 
#             model_name=model
#     )

#     if user_question:

#         prompt = ChatPromptTemplate.from_messages(
#             [
#                 SystemMessage(
#                     content=system_prompt
#                 ),  

#                 MessagesPlaceholder(
#                     variable_name="chat_history"
#                 ),  

#                 HumanMessagePromptTemplate.from_template(
#                     "{human_input}"
#                 ),  
#             ]
#         )

#         conversation = LLMChain(
#             llm=groq_chat, 
#             prompt=prompt, 
#             verbose=True,  
#             memory=memory,  
#         )
        
#         response = conversation.predict(human_input=user_question)
#         message = {'human':user_question,'AI':response}
#         st.session_state.chat_history.append(message)
#         st.write("Chatbot:", response)

# if __name__ == "__main__":
#     main()
import streamlit as st
from langchain.chains import LLMChain
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder

st.markdown("""
<style>
.chat-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 10px;
}

.user-message {
    background-color: #DCF8C6;
    color: black;
    max-width: 70%;
    border-radius: 10px;
    padding: 8px 12px;
    margin: 5px;
    align-self: flex-end;
}

.bot-message {
    background-color: #F0F0F0;
    color: black;
    max-width: 70%;
    border-radius: 10px;
    padding: 8px 12px;
    margin: 5px;
    align-self: flex-start;
}

.chat-input-container {
    width: 100%;
    padding: 10px;
    margin-top: 10px;
    border-radius: 20px;
    border: 1px solid #ccc;
    outline: none;
}
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'user_question' not in st.session_state:
        st.session_state.user_question = ''

def main():
    """
    This function is the main entry point of the application. It sets up the Groq client, the Streamlit interface, and handles the chat interaction.
    """
    
    groq_api_key = st.secrets["GROQ_API_KEY"]

    spacer, col = st.columns([5, 1])  
    with col:  
        st.image('VS_Logo.png')

    st.title("Venturesathi ESSP")
    st.write("Welcome to venturesathi ESSP. I can help answer your questions, provide information regarding attendance, leaves and other queries!")

    system_prompt = system_prompt = '''You are a  Human Resource Proffesional. You Have to provide the information about leave policies of the company,etc. 
    If you unable to answer give them the link to visit www.venturesathi.com
        Leave Policies: LEAVE POLICY
        Leave Entitlement for the year - Total leaves per employee for the year:
        1. 12 Public Holidays
        2. 2 Restricted/Optional Holidays
        Salient Features: -
        Flexible Leave and Encashment Policy Framework
        ▪ Leave encashment will occur upon completion of one year of employment 
        along with variable pay.
        a. Six-day working schedule: Employees working six days a week are entitled 
        to two days per month as paid leave.
        b. Weekend off Exception: Employees with a six days workweek, who have the 
        2nd and 4th Saturdays off, will also be entitled to two days per month as paid
        leave.
        c. Five working day exception: Employees working a standard five-day work
        week are not eligible for the two days per month paid leave policy.
        ▪ In the event of an employee leaving the company by following proper 
        procedures as laid down in company policies, accrued leave balances will be 
        subject to encashment.
        ▪ Carried forward leaves are limited to 24 days per calendar year.
        ▪ Employees can avail leave in case of sickness or in case of emergency, subject 
        to management’s discretion and approval. Entitlement is pro-rata from their 
        date of joining.
        ▪ All leaves need prior approval from the supervisor/line manager and should be 
        recorded in Workday. In case of sickness and emergency (exceptional 
        circumstances), the employee needs to inform the supervisor as soon as possible and record the leave in the system immediately on returning to duty.
        ▪ If the employee is not back in the office before the 1st of the next month, the 
        supervisor will record that leave in the system on the employee’s behalf so that 
        the leave records are updated on time. In the case of an emergency, employees 
        must notify their line manager as soon as practicable of their absence. If they 
        do not call within 4 hours of the scheduled time, they will be marked absent 
        for the day. Salary will be deducted even if there is leave available.
        ▪ Employees need to submit a Medical Certificate to their supervisor in case 
        they avail more than three days of leave under sickness. Every employee can 
        take 24 paid leaves in a year. The one monthly leave can be taken according to 
        employee discretion subject to prior one day notice and approval.
        ▪ Planned long leaves plan must be set at the beginning of the year with the 
        supervisor and should be approved two weeks before the date from which the 
        leave is to commence.
        ▪ Employees can avail themselves of a maximum of 5 working days of leave at 
        one time, subject to the superior's approval and discretion.
        ▪ Any leave request of more than five working days will be treated as a special 
        leave request and is subject to the approval and discretion of the management.
        ▪ Superior’s approval is guided by the criticality of the situation and the business 
        requirements.
        ▪ Management can take a discretionary decision on the maximum leaves availed 
        by an employee and may review the time limit. However, this will be on a case 
        to case basis and not set by any precedence.
        ▪ During the notice period, employees should not avail leave. If they do, at the 
        discretion &approval of their line manager, their notice period will be further 
        extended by the number of leave days availed.
        Human Resource Policies
        ▪ Any exceptions to this policy will be at the sole discretion of the management, 
        depending on the criticality of the case.
        ▪ Any breach of this policy can result in disciplinary action.
        ▪ Management reserves the right to change/amend the policy.
        Leave Without Pay (LWP):
        ▪ Any sanctioned leave which does not fall under any of the above categories 
        (i.e. Sick, Earned, Paternity or Maternity Leave) will be considered as Leave 
        without Pay.
        ▪ Leave taken over and above the leave sanctioned will be considered as an 
        absence unless applied for and sanctioned.
        ▪ In case of overstay of any leave and reasons for overstay not being sufficient, 
        the period of overstay will be continued to be treated as ABSENCE and can 
        call for disciplinary action. If leave is taken, it can be extended only after 
        approval by the concerned supervisor.
        ▪ In the case of LWP and ABSENCE, proportionate reductions will take place in 
        the following:
        ▪ Monthly salary, savings and other benefits.
        ▪ Annual reimbursements, bonuses and other entitlements.
        Public Holidays
        ▪ HR will circulate a list of all company holidays at the beginning of each 
        calendar year.
        ▪ This is our company's holiday policy that outlines all the days of the year that 
        we acknowledge as holidays. In other words, these are the days when our 
        employees don't work, and our offices are closed.
        ▪ This policy is applicable to all Venturesathi employees.
        Sl.no Date Day Occasion Optional/ National Holiday
        1 1-Jan Mon New Year Holiday
        2 26-Jan Fri Republic Day National Holiday
        3 8-Mar Fri Maha Shivaratri Optional Holiday
        4 25-Mar Mon Holi Holiday
        5 29-Mar Fri Good Friday Optional Holiday
        6
        9-Apr Tue
        Ugadi / Gudi Padwa
        / Vaisakh Optional Holiday
        7 11-Apr Thu Eid-ul-Fitar Optional Holiday
        8 17-Apr Wed Ramanavami Holiday
        9 14- Jun Fri Raja Parba Optional Holiday
        10 17-Jun Mon Eid al- Adha Optional Holiday
        11 7 Jul Sun Rath yatra Holiday
        12 17-Jul Wed Muharram Optional Holiday
        13 15-Aug Thu Independence Day National Holiday
        14 19-Aug Mon Raksha Bandhan Holiday
        15 26-Aug Mon Janmashtami Holiday
        16 7-Sep Sat Ganesh Chaturthi Holiday
        17 2-Oct Wed Gandhi Jayanti Holiday
        18 12-Oct Sat Dusshera Holiday
        19 1-Nov Fri Diwali Holiday
        20 7-Nov Thu Chhath Puja Optional Holiday
        21 25-Dec Wed Christmas Optional Holiday
        Venturesathi acknowledges the following holidays for the year 2024:
        *** Please note this holiday list applicable for 5 day working employees:
        Sl.no Date Day Occasion Optional/ National 
        Holiday
        1 1-Jan Mon New Year Optional Holiday
        2 26-Jan Fri Republic Day National Holiday
        3 8-Mar Fri Maha Shivaratri Optional Holiday
        4 25-Mar Mon Holi Holiday
        5 29-Mar Fri Good Friday Optional Holiday
        6 9-Apr Tue
        Ugadi / Gudi Padwa
        / Vaisakh Optional Holiday
        7 11-Apr Thu Eid-ul-Fitar Optional Holiday
        8 17-Apr Wed Ramanavami Holiday
        9 14- Jun Fri Raja Parba Optional Holiday
        10 17-Jun Mon Eid al- Adha Optional Holiday
        11 7 Jul Sun Rath yatra Holiday
        12 17-Jul Wed Muharram Optional Holiday
        13 15-Aug Thu Independence Day National Holiday
        14 19-Aug Mon Raksha Bandhan Holiday
        17 2-Oct Wed Gandhi Jayanti Holiday
        18 12-Oct Sat Dusshera Holiday
        19 1-Nov Fri Diwali Holiday
        20 7-Nov Thu Chhath Puja Optional Holiday
        21 25-Dec Wed Christmas Optional Holiday
        Please note:
        ▪ Employees are eligible to take all the National Holidays and up to a maximum
        of 2 of the Optional Holidays according to their convenience.
        ▪ Please inform your respective reporting managers before taking up any of the
        Optional Holidays.
        ▪ The employees are eligible to take a total of 14 Holidays (12+2)
        ▪ Please remember taking consecutive holidays on days like Saturday, Sunday
        and Monday will be considered as three days leave ( if an employee is taking
        leave on Saturday and Monday, then Sunday will also be considered as leave).
        ▪ Please remember that these days are considered days off at Venturesathi. This
        is true for all the employees unless a particular department, location or position 
        of the company must operate these days and stay available for
        customer/clients.
        Working on a holiday:
        ▪ If working on a holiday is necessary, we will inform all the employees in 
        advance. 
        ▪ We will compensate for that Holiday.
        Holiday pay entitlement policy.
        ▪ Full-time employees who don't work on a holiday will not see any reduction in
        their regular pay.
        ▪ Part-time employees will be paid based on the number of hours they would
        have worked if it wasn't a holiday.
        ▪ Temporary non-exempt employees are not entitled to holiday pay.
        Religious Holidays
        If there are any other religious holidays that our employees celebrate,
        Venturesathi will adhere to anti-discrimination best practices and allow these
        employees to take paid time off.
        (Note: Venturesathi has the rights to change the Leave policy as per
        requirements)

        For Applying Leaves and Marking thier attendance suggest them to login into jio attendance Mobile app and navigate to menus ex - Leave, attendace etc. if they don't have
        the app suggest them to dowanload by this link and login by thier Mobile Number registered in company.
        Jio Attendance download link https://jioattendance.jio.com/map/download_app.html.
        If they face any issue suggest them to contact Sipra Soni Pradhan - HR Executive or drop a mail to hr@venturesathi.com
        
        Provide the answers of queries related to leaves by reffering this. try to be polite and don't answer leave queries out of this information.

        ATTENDANCE AND PUNCTUALITY GUIDELINES -
        The standard workweek schedule for all teams is as follows:
        Monday to 
        Saturday Grace Period Team name
        Work 
        Shift 9:30 AM – 6:30 PM 5MIN (9:35AM) Applicable for all the departments
        The Dedicated Resources/ Employees working out of Client offices at various 
        locations are requested to follow the work timings and schedule as per the client 
        office guidelines. Any changes in the client schedule should be informed to the 
        HR Team. 
        Workdays and Weekly offs will be as per client allocation/deployment
        (Monday to Friday or Monday to Saturday).
        A full workday is considered only when you work for 8 hours starting from 
        your stipulated time, and a half-day will be considered only when you work for 
        4.5 hours/ less (excluding the lunch/food break) starting from your stipulated 
        time. Saturday’s full-day working will be considered on completion of 8 hours.
        (the maximum limit of work hours in a day has been increased from 9 to 12 in a 
        day, if the employers provide 3 weekly offs in a week – New Labour Law 
        Code 2022)
        In the event of absence or tardiness from an assigned work schedule, the 
        employee is required to report the absence to the Company. When reporting an 
        absence, the employee must E-mail / Telephone/ in Company stipulated channel 
        his or her supervisor and authorized HR representative only. The employee 
        must report within two hours of the scheduled start time.
        An employee’s absence will be deemed unexcused when an employee fails to 
        call in, gives a late notice, fails to give advance notice for an absence which 
        could be anticipated, exceeds the number of length of absences as defined by 
        policy or authorized in advance by the Supervisor or HR. Unexcused/ 
        uninformed absentees are subject to corrective disciplinary action.
        Location Heads/ Supervisors / Leads / Clients (wherever applicable) in the 
        respective location are requested to be alert and report us of any absence or 
        tardiness of employees in their respective locations.
        Following are some points and measures that are taken, and we would like 
        every employee to remember them categorically and take a note of this:
        Attendance Entry
        • For any attendance (IN time or OUT time) not registered on a 
        given day, the first work e-mail (IN time) and the last work e-mail (OUT 
        Time) for the day will be considered along with a notification sent to the 
        HR Team. 
        This is applicable for all instances like (Forgot to Clock in or Clock out –
        online or biometric or JIO Attendance)
        • For any biometric registration not happening/ reflecting, there is a 
        backend file which captures your attendance for the day irrespective if it 
        does not get synced with the Online System. The same shall be referred 
        for correction and time reference.
        • If still in doubts, accountability, approval from the supervisor 
        keeping Human Resource on CC will be taken.
        • Anyone having any issues or challenges regarding their bio-metric 
        registrations has to be immediately brought to the notice
        Late marks
        • Any extra minute above the stipulated Office timings will be 
        considered to be a ‘late mark’.
        • Any late coming, informed or uninformed will be marked under 
        ‘late mark’, and deductions will be made wherever applicable as per the 
        rules and guidelines defined.
        • If an employee report working after 2.00 p.m., it will be considered 
        as Half Day leave/salary deduction.
        • A group of three ‘late marks’ will result in a deduction of one-half 
        day from your balance leaves/salary.
        Working home/ Official Tour
        If any employee is on ‘official tour’ or on ‘work from home/ outdoor 
        duty’, he/she must have a mail approval from the highest reporting 
        authority of his Department in charge and submit it to the HR department 
        for his attendance registration.
        • The absence of any official intimation will be deemed as ‘unauthorized absent’ and would be adjusted from your balance 
        leaves/salary.
        • Work from home is approved only with the prior notification to 
        the Senior Management(If applicable). More than once will be deemed 
        as Leave taken and will be adjusted from the leave balance/salary.
        • Work from home employees should be available online 
        (Email/Teams/WhatsApp/SMS) and accessible/ responsive at all times 
        during the 9 hours of duty.
        • Leave early
        • In case any employee has to move out of the office for any 
        personal reason except during lunch hours, he/she is required to get prior 
        approval from his/her immediate supervisor and keep HR posted.

        Provide the answers of queries related to Attendance by reffering this. try to be polite and don't answer attendace queries out of this information.
                '''

    model = 'llama3-8b-8192'
    conversational_memory_length = 2

    initialize_session_state()
    memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)

    for message in st.session_state.chat_history:
        if message['human']:
            st.markdown(f'<div class="chat-container"><div class="user-message">{message["human"]}</div></div>', unsafe_allow_html=True)
        if message['AI']:
            st.markdown(f'<div class="chat-container"><div class="bot-message">{message["AI"]}</div></div>', unsafe_allow_html=True)

    user_question = st.text_input("You:", key="user_question", help="Press Enter to send", value=st.session_state.user_question)

    if user_question:
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content=system_prompt
                ),  

                MessagesPlaceholder(
                    variable_name="chat_history"
                ),  

                HumanMessagePromptTemplate.from_template(
                    "{human_input}"
                ),  
            ]
        )

        conversation = LLMChain(
            llm=ChatGroq(groq_api_key=groq_api_key, model_name=model),
            prompt=prompt, 
            verbose=True,  
            memory=memory,  
        )

        response = conversation.predict(human_input=user_question)
        message = {'human': user_question, 'AI': response}
        st.session_state.chat_history.append(message)

        st.markdown(f'<div class="chat-container"><div class="user-message">{user_question}</div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="chat-container"><div class="bot-message">{response}</div></div>', unsafe_allow_html=True)

    st.write("Powered By: Venturesathi")

if __name__ == "__main__":
    main()
