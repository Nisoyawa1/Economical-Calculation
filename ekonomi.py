import streamlit as st 
import pandas as pd

st.title('Economic Calculation')
st.caption('by Nisoyawa')
st.header('Input the data value')



oil_lifting_cost=20
Gas_injection_Price=6000
workover_cost=300000


banyaknya_hari = st.number_input('Numbers of day')
st.write('The current number is ', banyaknya_hari)
banyaknya_hari=int(banyaknya_hari)

optimum_gas_injection = st.number_input('Optimum gas injection Rate')
st.write('The current number is ', optimum_gas_injection)


water_cut = st.number_input('Water cut in%')
st.write('The current number is ', water_cut)


liquid_rate = st.number_input('Liquid rate')
st.write('The current number is ', liquid_rate)


oil_rate = liquid_rate*(1-water_cut/100)

tubing_pressure = st.number_input('Tubing Pressure')
st.write('The current number is ', tubing_pressure)

Tubing_ID = st.number_input('Tubing ID')
st.write('The current number is ', Tubing_ID)

harga_minyak = st.number_input('Oil Price')
st.write('The current number is ', harga_minyak)


oil_production=[]
oil_revenue=[]
liftitng_cost=[]
injection_gas=[]
banyaknya_hari=banyaknya_hari+1

for i in range (1,banyaknya_hari):    #Mau buat oil production sama kayak banyak inputan hari
    oil_production.append(oil_rate)


for j in oil_production:                #mau buat harga oil revenue
    j=float(j)
    j=j*harga_minyak
    oil_revenue.append(j)

for j in oil_production:            #mau buat oil lifting cost
    j=j*oil_lifting_cost
    liftitng_cost.append(j)

for j in range (0,banyaknya_hari):                  #mau itung nilai injection gas
    itung=Gas_injection_Price*optimum_gas_injection
    injection_gas.append(itung)

investment=[300000]
for j in range (1,banyaknya_hari):              #mau masukin nilai investment yang sblmnya udah ada listnya
    j=0
    investment.append(j)

Profit=[]
cumulative=[]
cumulative_1=[]

matiin=0                    #mau buat profit
for i,j,k,o in zip(oil_revenue,liftitng_cost,injection_gas,investment):
    sip=(i-j-k-o)
    Profit.append(sip)


mati=0
for j in Profit:        #mau buat cummulative tapi awalnya aja 
    if mati==0:
        cumulative.append(j)
    elif mati !=0:
        cumulative.append(0)
    mati=+1

y=0
for x in range (0,len(Profit)):         #mau cari cumulative
    y+=Profit[x]
    cumulative_1.append(y)

kata_kata=[]                #buat paid atau belom paidnya 
for j in range (0,len(cumulative_1)):
    if cumulative_1[j]>0:
       kata_kata.append('Paid')
    else:
        kata_kata.append('Not yet Paid')

hari=[]
for j in range (0,banyaknya_hari):
    days=j+1
    hari.append(days)

df=pd.DataFrame(list(zip(hari,oil_production,oil_revenue,liftitng_cost,injection_gas,investment,Profit,cumulative_1,kata_kata)),
                columns=['Days','Oil production','oil revenue', 'lifting cost', 'injection gas','investment','profit','cumulative','Pay Out Time'])
hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

st.header('Output Table')
# Display an interactive table
st.dataframe(df)
