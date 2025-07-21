import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib as plt

st.set_page_config(page_title="DASHBOARD", page_icon=":bar_chart:",layout="wide")
st.title(" 👷🏼‍♂️:blue[ EMPLOYEES DASHBOARD]",width='stretch')

st.markdown('<style>div.block-container{padding-top:5rem;}</style>',unsafe_allow_html=True)


d={'empid':pd.Series([1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
                     index=[1,2,3,4,5,6,7,8,9,10]),
                     'Ename':pd.Series(['Smith','Blake','King','Harry','Mohit','Harry','Pawan','perry','jerry','gagan'],
                     index=[1,2,3,4,5,6,7,8,9,10]),
                     'Job':pd.Series(['manager','salesmen','president','clerk','programmer','clerk','programmer','clerk','manager','salesmen',],
                     index=[1,2,3,4,5,6,7,8,9,10]),
                     'salary':pd.Series([55000,65000,85000,25000,55000,25000,65000,25000,35000,45000],
                     index=[1,2,3,4,5,6,7,8,9,10]),
                     'comm':pd.Series([100,200,100,500,300,500],
                     index=[1,3,5,7,9,10]),
                     'Deptno':pd.Series([10,20,10,10,30,10,20,10,30,40],
                     index=[1,2,3,4,5,6,7,8,9,10])
                     }
df=pd.DataFrame(d)
st.dataframe(df)

col1,col2=st.columns([.45,0.55])
with col1:
    st.text('  ')

with col2:
    st.subheader("DATA ANALYSIS")

col3,col4=st.columns([0.5,0.5])
with col3:
    fig=px.bar(df,x='Ename',y='salary',title='BarGraph',height=500,template='gridon',color='Ename')
    st.plotly_chart(fig,use_container_width=True)

with col4:
    fig=px.line(df,x='Ename',y='salary',title='LineGraph',height=500,template='gridon')
    st.plotly_chart(fig,use_container_width=True)




col5,col6=st.columns([.5,.5])
with col5:
    fig=px.sunburst(df ,title='Sunburst',
        path=['empid', 'Job','salary'],
        values='salary',width=350,
        height=500,template='gridon')
    st.plotly_chart(fig,use_container_width=True)

with col6:
    fig=px.pie(df,names='Job',values='Deptno', width=600,
               title='Pie Chart',
                height=500,template='gridon')
    st.plotly_chart(fig,use_container_width=True)


_,col7=st.columns([.1,.9])
with col7:
    fig=px.treemap(df,path=[ 'Job','Ename','salary'],title='Tree Map',
                height=500,template='gridon')
    st.plotly_chart(fig,use_container_width=True)