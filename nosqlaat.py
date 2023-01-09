import streamlit as st
# import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import numpy as np


from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
cluster = Cluster()
cloud_config= {
         'secure_connect_bundle': 'secure-connect-nosql.zip'
}
auth_provider = PlainTextAuthProvider('AcxPrfPZsBHEZwPXwDAvurCt', 'pJURS4ghZSOupiZSKcEu8-kBH,pJbS-bsD01v5-l2OXHtR5+BNXUmP0vc46wO3qOt7G7K4.cIQF5EpfSDhMKraq5wI668fI,beZ+oi.rr442Ob8BILDZ3E4IFCQ+ZM_j')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()


session = cluster.connect('mental_health')










q=session.execute("select count(*) from aat_survey where country='Canada' and treatment='Yes'")
r=str(q[0])
s=r.split(":")
t=str(s[0]).split("=")
u=str(t[1]).split(")")
int_value1=int(u[0])
# st.write(int_value1)

q=session.execute("select count(*) from aat_survey where country='Canada' and treatment='No'")
r=str(q[0])
s=r.split(":")
t=str(s[0]).split("=")
u=str(t[1]).split(")")
int_value2=int(u[0])
# st.write(int_value2)

st.write("Canada")
labels = 'People who have sought treatment for a mental health condition', 'People who have not sought treatment for a mental health condition'
sizes = [int_value1, int_value2]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)








q=session.execute("select count(*) from aat_survey where country='United States' and treatment='Yes'")
r=str(q[0])
s=r.split(":")
t=str(s[0]).split("=")
u=str(t[1]).split(")")
int_value1=int(u[0])
# st.write(int_value1)

q=session.execute("select count(*) from aat_survey where country='United States' and treatment='No'")
r=str(q[0])
s=r.split(":")
t=str(s[0]).split("=")
u=str(t[1]).split(")")
int_value2=int(u[0])
# st.write(int_value2)

st.write("United States")
labels = 'People who have sought treatment for a mental health condition', 'People who have not sought treatment for a mental health condition'
sizes = [int_value1, int_value2]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)







q=session.execute("select count(*) from aat_survey where tech_company='Yes' and treatment='Yes'")
r=str(q[0])
s=r.split(":")
t=str(s[0]).split("=")
u=str(t[1]).split(")")
int_value1=int(u[0])
# st.write(int_value1)

q=session.execute("select count(*) from aat_survey where tech_company='Yes' and treatment='No'")
r=str(q[0])
s=r.split(":")
t=str(s[0]).split("=")
u=str(t[1]).split(")")
int_value2=int(u[0])
# st.write(int_value2)

st.write("People working for a tech company")
labels = 'People who have sought treatment for a mental health condition', 'People who have not sought treatment for a mental health condition'
sizes = [int_value1, int_value2]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)








q=session.execute("select count(*) from aat_survey where tech_company='No' and treatment='Yes'")
r=str(q[0])
s=r.split(":")
t=str(s[0]).split("=")
u=str(t[1]).split(")")
int_value1=int(u[0])
# st.write(int_value1)

q=session.execute("select count(*) from aat_survey where tech_company='No' and treatment='No'")
r=str(q[0])
s=r.split(":")
t=str(s[0]).split("=")
u=str(t[1]).split(")")
int_value2=int(u[0])
# st.write(int_value2)

st.write("People not working for a tech company")
labels = 'People who have sought treatment for a mental health condition', 'People who have not sought treatment for a mental health condition'
sizes = [int_value1, int_value2]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)





q=session.execute("select count(*) from aat_survey where remote_work='Yes' and treatment='Yes'")
r=str(q[0])
s=r.split(":")
t=str(s[0]).split("=")
u=str(t[1]).split(")")
int_value1=int(u[0])
# st.write(int_value1)

q=session.execute("select count(*) from aat_survey where remote_work='No' and treatment='Yes'")
r=str(q[0])
s=r.split(":")
t=str(s[0]).split("=")
u=str(t[1]).split(")")
int_value2=int(u[0])
# st.write(int_value2)

st.write("People who have sought treatment for a mental health condition")
labels = 'People working remotely', 'People not working remotely'
sizes = [int_value1, int_value2]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)













form = st.form(key='my_form')
ans={}
# rows = session.execute('SELECT * FROM aat_survey;')
# st.write(rows[0])
# st.write("Hi")
# columns = session.execute('SELECT * FROM system.schema_columns WHERE columnfamily_name = mhtable;')
columns = session.execute('SELECT column_name FROM system_schema.columns WHERE keyspace_name = \'mental_health\' AND table_name = \'aat_survey\';')
# st.write(columns)

count=session.execute('select count from aat_survey where id=-1 and age=-1')
# st.write(count[0])
z=str(count[0])
c=z.split(":")
# st.write(c[0])
# o=str(c).split("'")
# st.write(o[1])
o=str(c[0]).split("=")
# st.write(n[1])
d=str(o[1]).split(")")
# st.write(l[0])
int_count=int(d[0])
# st.write(int_count)

# # st.write(columns[1])
# x=str(columns[0])
# a=x.split(":")
# # st.write(a[0])
# m=str(a).split("'")
# st.write(m[1])

# columns=column.split()
# st.write(len(columns))
# st.write(np.size(columns,0))

# columns=str(column)
# st.write(columns)

for i in range(0,int_count):
    x=str(columns[i])
    a=x.split(":")
    m=str(a).split("'")

    if(m[1]=="id"):
        continue
    if(m[1]=="count"):
        continue
    if(m[1]=="treatment"):
        flag=i
    if(m[1]=="age"):
        flag_age=i
    ans["string{0}".format(i)] =form.text_input(label=m[1],key=i)
new_field=form.text_input(label="New field",key=i+1)
new_field_ans=form.text_input(label="Value",key=i+2)
submit_button = form.form_submit_button(label='Submit')
if submit_button:
    if(len(ans["string{0}".format(flag)]) is 0):
        st.error("Enter Yes or No for treatment")
    elif(len(ans["string{0}".format(flag_age)]) is 0):
        st.error("Enter age")
    elif(len(new_field) is 0 and len(new_field_ans)>0):
        st.error("Give the new field name")
    elif(len(new_field)>0 and len(new_field_ans) is 0):
        st.error("Give value for the new field")
    else:
        # st.write("Input now")
    
        id=session.execute("select max(id) from aat_survey;")
        # st.write(id[0])
        y=str(id[0])
        b=y.split(":")
        # st.write(b[0])
        n=str(b[0]).split("=")
        # st.write(n[1])
        l=str(n[1]).split(")")
        # st.write(l[0])
        int_id=int(l[0])
        next_id=int_id+1
        # st.write(next_id)
        # session.execute(f"INSERT INTO aat_survey (id,age) VALUES ({next_id},20)")

        for i in range(0,int_count):
            x=str(columns[i])
            a=x.split(":")
            m=str(a).split("'")

            if(m[1]=="id"):
                continue
            if(m[1]=="count"):
                continue

            answer=ans["string{0}".format(i)]
            if(len(answer) is 0):
                continue
            # st.write(m[1])
            # st.write(answer)
            


            # session.execute( """INSERT INTO aat_survey (%s) VALUES (%s)""",(m[1], answer))
            # session.execute( "INSERT INTO aat_survey (%s) VALUES (%s)",[m[1]],[answer])


            # session.execute(f"INSERT INTO aat_survey ({m[1]}) VALUES ({answer}) where id={next_id}")
            if(m[1]=="age"):
                # session.execute(f"UPDATE aat_survey set {m[1]} = {answer} where id={next_id}")
                session.execute(f"INSERT INTO aat_survey (id,age) VALUES ({next_id},{answer})")
                age=answer
            else:
                session.execute(f"UPDATE aat_survey set {m[1]} = '{answer}' where id={next_id} and age={age}")

        #add new field and value
        if(len(new_field)>0 and len(new_field_ans)>0):
            session.execute( f"ALTER TABLE aat_survey ADD {new_field} text")
            session.execute(f"UPDATE aat_survey set {new_field} = '{new_field_ans}' where id={next_id} and age={age}")
            new_count=int_count+1
            session.execute(f"UPDATE aat_survey set count = {new_count} where id=-1 and age=-1")


# select count(*) from aat_survey where country='Canada' and treatment='Yes';
# select count(*) from aat_survey where country='Canada' and treatment='No';

# select count(*) from aat_survey where country='United States' and treatment='Yes';
# select count(*) from aat_survey where country='United States' and treatment='No';

# select count(*) from aat_survey where tech_company='Yes' and treatment='No';
# select count(*) from aat_survey where tech_company='Yes' and treatment='Yes';

# select count(*) from aat_survey where tech_company='No' and treatment='No';
# select count(*) from aat_survey where tech_company='NO' and treatment='Yes';

# select count(*) from aat_survey where remote_work='Yes' and treatment='Yes';
# select count(*) from aat_survey where remote_work='No' and treatment='Yes';














# import streamlit as st
# from streamlit_chat import message
# import streamlit.components.v1 as components

# form = st.form(key='my_form')
# ans={}
# # columns = session.execute('SELECT column_name FROM system.schema_columns WHERE keyspace_name = 'KeySpaceName' AND columnfamily_name = 'TableName';')
# for i in range(0,2):
#     a="asd"
#     ans["string{0}".format(i)] =form.text_input(label=a,key=i)
# new_field=form.text_input(label="New field",key=i)
# new_field_ans=form.text_input(label="Value",key=i+1)
# submit_button = form.form_submit_button(label='Submit')
# if submit_button:
#     #st.write(f'hello {name}')
#     # for i in range(0,2):
#     #     st.write(ans["string{0}".format(i)])
#     # st.write(new_field)
#     # st.write(new_field_ans)
#     if(len(new_field) is 0 and len(new_field_ans)>0):
#         st.error("Give the new field name")
#     elif(len(new_field)>0 and len(new_field_ans) is 0):
#         st.error("Give value for the new field")
#     else:
#         st.write("Input now")

























# import streamlit as st
# from streamlit_chat import message
# import streamlit.components.v1 as components

# form = st.form(key='my_form')
# ans={}
# # columns = session.execute('SELECT column_name FROM system.schema_columns WHERE keyspace_name = 'KeySpaceName' AND columnfamily_name = 'TableName';')
# ans["string{0}".format(1)] =form.text_input(label="age",key=1)
# ans["string{0}".format(2)] =form.text_input(label="anonimity",key=2)
# ans["string{0}".format(3)] =form.text_input(label="benefits",key=3)
# ans["string{0}".format(4)] =form.text_input(label="care options",key=4)
# ans["string{0}".format(5)] =form.text_input(label="country",key=5)
# ans["string{0}".format(6)] =form.text_input(label="co-workers",key=6)
# ans["string{0}".format(7)] =form.text_input(label="family history",key=7)
# ans["string{0}".format(8)] =form.text_input(label="gender",key=8)
# ans["string{0}".format(9)] =form.text_input(label="id",key=9)
# ans["string{0}".format(10)] =form.text_input(label="leave",key=10)
# ans["string{0}".format(11)] =form.text_input(label="mental_health_consequence",key=11)
# ans["string{0}".format(12)] =form.text_input(label="mental_health_interview",key=12)
# ans["string{0}".format(13)] =form.text_input(label="mental_vs_physical",key=13)
# ans["string{0}".format(14)] =form.text_input(label="no_employees",key=14)
# ans["string{0}".format(15)] =form.text_input(label="obs_consequence",key=15)
# ans["string{0}".format(16)] =form.text_input(label="phys_health_consequemce",key=16)
# ans["string{0}".format(17)] =form.text_input(label="phys_health_interview",key=17)
# ans["string{0}".format(18)] =form.text_input(label="remote_work",key=18)
# ans["string{0}".format(19)] =form.text_input(label="seek_help",key=19)
# ans["string{0}".format(20)] =form.text_input(label="self_employed",key=20)
# ans["string{0}".format(21)] =form.text_input(label="state",key=21)
# ans["string{0}".format(22)] =form.text_input(label="supervisoe",key=22)
# ans["string{0}".format(23)] =form.text_input(label="tech_company",key=23)
# ans["string{0}".format(24)] =form.text_input(label="treatment",key=24)
# ans["string{0}".format(25)] =form.text_input(label="wellness_program",key=25)
# ans["string{0}".format(26)] =form.text_input(label="work_interfere",key=26)

# new_field=form.text_input(label="New field",key=27)
# new_field_ans=form.text_input(label="Value",key=28)
# submit_button = form.form_submit_button(label='Submit')
# if submit_button:
#     #st.write(f'hello {name}')
#     # for i in range(0,2):
#     #     st.write(ans["string{0}".format(i)])
#     # st.write(new_field)
#     # st.write(new_field_ans)
#     if(len(new_field) is 0 and len(new_field_ans)>0):
#         st.error("Give the new field name")
#     elif(len(new_field)>0 and len(new_field_ans) is 0):
#         st.error("Give value for the new field")
#     else:
#         st.write("Input now")
