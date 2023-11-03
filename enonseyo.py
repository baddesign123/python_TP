# enonse1
chen1="jodi a se 2 novanm"
chen_miniskil=chen1.lower()
# print(chen_miniskil)


#enonse2
chen2="Ayiboobo Ayiti"
chendekoupe=chen2.split(" ")
# print(chendekoupe)


#enonse3
chen3="ayibobo ayiti cheri men nou"
chen_modiffye=chen3.title()
# print(chen_modiffye)


#enonse4
chen4="Ayibobo Ayiti men nou"
chen_koupe=chen4.split(" ")
inisyal=""
for i in chen_koupe:
    inisyal+=i[0]
# print(inisyal.upper())


#enonse5
chen5="Ayibobo Ayiti men nou rele anmwey"
chen_ranplase=chen5.replace("a","@")
# print(chen_ranplase)


#enonse6
chen6="Ayiti"
movire=""
long=len(chen6)-1
while long>=0:
    movire+=(chen6[long]).upper()
    long-=1
# print(movire)


# enonse7
chen7="Ayiti kapab avanse"
pos=0
i=0
for element in chen7:
    if element =="a":
        pos=i
        break
    i+=1

# if pos ==0:
#     print("Pa gen a nan chenn sa")
# else:
#     print(f"Pozisyon premye 'a' a se {pos}")


#enonse8
chen8="Ayiti kapab avanse"
total=0
i=0
for element in chen8:
    let=element.lower()
    if let=="a":
        total+=i
    i+=1

# if total ==0:
#     print("Pat gen a nan chen nan")
# else:
#     print(total)


#enonse9
chen9="Ayiti kapab avanse"
lis9=[]
i=0

for element in chen9:
    if element=="a":
        lis9.append(i)
    i+=1

# if(len(lis9)==0):
#     print("Pat gen a nan chenn nan")
# else:
#     print(lis9)



#enonse10
chen10="Ayiti kapab avanse"
chen_final=chen10.replace(" ","")
chen_final+=str(len(chen_final))
# print(chen_final)



#enonse11
lis_eleman11=[]
n=20
i=0
existe=False
while i<=n:
    if i%2==0:
        lis_eleman11.append(i)
        existe=True
    i+=1
# if existe:
#     print(lis_eleman11)
# else:
#     print("Pat gen eleman divizib pa 2 nan lis la")



#enonse12
lis_antye12=[1,2,3,4,5,6]
i=0
while i<len(lis_antye12):
    lis_antye12[i]=str(lis_antye12[i])
    i+=1
# print(lis_antye12)


#enonse13

lis_chenn13=["badio", "nicolas", "hector", "payen", "bazelais","pierre louis"]
i=0
while i<len(lis_chenn13):
    lis_chenn13[i]=lis_chenn13[i].upper()
    i+=1
# print(lis_chenn13)



#enonse14
lis_element14=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
i=0
nouvo_lis14=[]
while i<len(lis_element14):
    if(i%3==0):
        nouvo_lis14.append(lis_element14[i])
    i+=1
# print(nouvo_lis14)


#enonse15
lis_inisyal15=[1,2,3,4,5,6,7,8,9]
lis_groupe15=[]
for i in range (0, len(lis_inisyal15),3):
    lis_groupe15.append(tuple(lis_inisyal15[i:i+3]))
# print(lis_groupe15)


#enonse16
lis16=[1,2,3,4,5,6,7,8,9,1,2,4,5,8,9]
lis_filtre16=[]
i=0
while i<len(lis16):
    if lis16[i] not in lis_filtre16:
        lis_filtre16.append(lis16[i])
    i+=1
# print(lis_filtre16)

#enonse17
lis17=[1,2,3,4,5,6,7,8,9,10]
lis17_1=[2,4,6,8,10]
lis17_2=[]

for element in lis17:
    if element in lis17_1:
        lis17_2.append(element)
# print(lis17_2)


#enonse18
lis18=[1,2,3,4,5,6,7,8,9,10]
lis18_1=[2,4,6,8,10]
lis18_2=[]

for element in lis18:
    if element not in lis18_1:
        lis18_2.append(element)
print(lis18_2)










