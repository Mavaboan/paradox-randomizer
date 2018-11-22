import random

#All countries added!!
#The different countrys numbers added automaticly and starts with 0
countries = [
    "Denmark", 
    "Norway", "Finland", "UK", "USA", "Soviet Union", 
    "Poland",  "Ireland", "Sweden", "Germany", "France", #10
    "Spain", "Italy", "Japan", "Iceland", "Lithuania", 
    "Estonia", "Latvia", "Romania", "Yugoslavia", "Serbia", #20
    "Greece", "Albania", "Bulgaria", "Hungary", "Croatia", 
    "Slovakia", "Luxemborg", "Belgium", "Netherlands", "Czechoslovakia", #30
    "Austria", "Portugal", "Switzerland", "Afghanistan", "Iraq", 
    "Oman", "Iran", "Saudi Arabia", "Turkey", "Yemen", #40
    "Egypt", "Syria", "Lebonon", "Jordan", "Libya", 
    "Australia", "New Zealand", "Bhutan", "Tibet", "Nepal", #50
    "British Raj", "Philipines", "Siam", "China", "Guangxi Clique", 
    "Peoples Republic of China", "Shanxi", "Xibei San Ma", "Sinkian", "Yunnan", #60
    "Mongolia", "Mengkukuo", "Tannu Tuva", "Korea", "Liberia", 
    "Ethiopia", "South Africa", "Canada", "Mexico", "Costa Rica", #70
    "El Salvadore", "Guatamala", "Honduras", "Nicaragua", "Panama", 
    "Cuba", "Dominican Republic", "Haiti", "Brazil", "Argentina", #80
    "Chile", "Colombia", "Bolivia", "Ecuador", "Paraguay", 
    "Peru", "Uruguay", "Venezuela"
]

print(len(countries))
#!! Need hardcode the country flags into the code !!
#Finds out how many countries there are
country_amount = len(countries)
#Finds a random number between 0 and the amount of countries we have
random_number = random.randint(0,country_amount)
#Prints a text telling user wich country 
#Will be deleted later on when GUI is finished
print("Your country is gonna be")
#Prints the name of a country from the list, based on the random number
print(countries[random_number])
print(random_number)

def country_flag():
    if countries[random_number] == countries[0]:
        print("DEN_democratic.tga")
    elif countries[random_number] == countries[1]:
        print("NOR_democratic.tga")
    elif countries[random_number] == countries[2]:
        print("FIN_neutrality.tga")
    elif countries[random_number] == countries[3]:
        print("ENG_democratic.tga")
    elif countries[random_number] == countries[4]:
        print("USA_democratic.tga")
    elif countries[random_number] == countries[5]:
        print("SOV_communism.tga")
    elif countries[random_number] == countries[6]:
        print("POL_neutrality.tga")
    elif countries[random_number] == countries[7]:
        print("IRE_democratic.tga")
    elif countries[random_number] == countries[8]:
        print("SWE_democratic.tga")
    elif countries[random_number] == countries[9]:
        print("GER_facsism.tga")
    elif countries[random_number] == countries[10]:
        print("FRA_democratic.tga")
    elif countries[random_number] == countries[11]:
        print("SPR_democratic.tga")
    elif countries[random_number] == countries[12]:
        print("ITA_facsism.tga")
    elif countries[random_number] == countries[13]:
        print("JAP_facsism.tga")
    elif countries[random_number] == countries[14]:
        print("flag")
    elif countries[random_number] == countries[15]:
        print("LIT_neutrality.tga")
    elif countries[random_number] == countries[16]:
        print("EST_neutrality.tga")
    elif countries[random_number] == countries[17]:
        print("LAT_neutrality.tga")
    elif countries[random_number] == countries[18]:
        print("ROM_neutrality.tga")
    elif countries[random_number] == countries[19]:
        print("YUG_neutrality.tga")
    elif countries[random_number] == countries[20]:
        print("flag")
    elif countries[random_number] == countries[21]:
        print("GRE_neutrality.tga")
    elif countries[random_number] == countries[22]:
        print("ALB_neutrality.tga")
    elif countries[random_number] == countries[23]:
        print("BUL_neutrality.tga")
    elif countries[random_number] == countries[24]:
        print("HUN_facsism.tga")
    elif countries[random_number] == countries[25]:
        print("flag")
    elif countries[random_number] == countries[26]:
        print("SLO_facsism.tga")
    elif countries[random_number] == countries[27]:
        print("LUX_democratic.tga")
    elif countries[random_number] == countries[28]:
        print("flag")
    elif countries[random_number] == countries[29]:
        print("HOL_democratic.tga")
    elif countries[random_number] == countries[30]:
        print("CZE_democratic.tga")
    elif countries[random_number] == countries[31]:
        print("AUS_neutrality.tga")
    elif countries[random_number] == countries[32]:
        print("POR_neutrality.tga")
    elif countries[random_number] == countries[33]:
        print("SWI_democratic.tga")
    elif countries[random_number] == countries[34]:
        print("AFG_neutrality.tga")
    elif countries[random_number] == countries[35]:
        print("IRQ_neutrality.tga")
    elif countries[random_number] == countries[36]:
        print("OMA_neutrality.tga")
    elif countries[random_number] == countries[37]:
        print("PER_neutrality.tga")
    elif countries[random_number] == countries[38]:
        print("SAU_neutrality.tga")
    elif countries[random_number] == countries[39]:
        print("TUR_neutrality.tga")
    elif countries[random_number] == countries[40]:
        print("YEM_neutrality.tga")
    elif countries[random_number] == countries[41]:
        print("flag")
    elif countries[random_number] == countries[42]:
        print("PHI_democratic.tga")
    elif countries[random_number] == countries[43]:
        print("SIA_facsism.tga")
    elif countries[random_number] == countries[44]:
        print("flag")
    elif countries[random_number] == countries[45]:
        print("GXC_neutrality.tga")
    elif countries[random_number] == countries[46]:
        print("AST_democratic.tga")
    elif countries[random_number] == countries[47]:
        print("NZL_democratic.tga")
    elif countries[random_number] == countries[48]:
        print("BHU_neutrality.tga")
    elif countries[random_number] == countries[49]:
        print("TIB_neutrality.tga")
    elif countries[random_number] == countries[50]:
        print("NEP_neutrality.tga")
    elif countries[random_number] == countries[51]:
        print("RAJ_neutrality.tga")
    elif countries[random_number] == countries[52]:
        print("MEN_facsism.tga")
    elif countries[random_number] == countries[53]:
        print("SIA_neutrality.tga")
    elif countries[random_number] == countries[54]:
        print("CHI_neutrality.tga")
    elif countries[random_number] == countries[55]:
        print("LIB_democratic.tga")
    elif countries[random_number] == countries[56]:
        print("PRC_communism.tga")
    elif countries[random_number] == countries[57]:
        print("SHX_neutrality.tga")
    elif countries[random_number] == countries[58]:
        print("XSM_neutrality.tga")
    elif countries[random_number] == countries[59]:
        print("SIK_communism.tga")
    elif countries[random_number] == countries[60]:
        print("YUN_neutrality.tga")
    elif countries[random_number] == countries[61]:
        print("MON_communism.tga")
    elif countries[random_number] == countries[62]:
        print("flag")
    elif countries[random_number] == countries[63]:
        print("TAN_communism.tga")
    elif countries[random_number] == countries[64]:
        print("flag")
    elif countries[random_number] == countries[65]:
        print("flag")
    elif countries[random_number] == countries[66]:
        print("ETH_neutrality.tga")
    elif countries[random_number] == countries[67]:
        print("SAF_democratic.tga")
    elif countries[random_number] == countries[68]:
        print("CAN_democratic.tga")
    elif countries[random_number] == countries[69]:
        print("MEX_neutrality.tga")
    elif countries[random_number] == countries[70]:
        print("COS_democratic.tga")
    elif countries[random_number] == countries[71]:
        print("ELS_facsism.tga")
    elif countries[random_number] == countries[72]:
        print("GUA__neutrality.tga")
    elif countries[random_number] == countries[73]:
        print("HON_democratic.tga")
    elif countries[random_number] == countries[74]:
        print("NIC_democratic.tga")
    elif countries[random_number] == countries[75]:
        print("PAN_democratic.tga")
    elif countries[random_number] == countries[76]:
        print("CUB_democratic.tga")
    elif countries[random_number] == countries[77]:
        print("DOM_facsism.tga")
    elif countries[random_number] == countries[78]:
        print("HAI_democratic.tga")
    elif countries[random_number] == countries[79]:
        print("BRA_neutrality.tga")
    elif countries[random_number] == countries[80]:
        print("ARG_neutrality.tga")
    elif countries[random_number] == countries[81]:
        print("CHL_democratic.tga")
    elif countries[random_number] == countries[82]:
        print("COL_democratic.tga")
    elif countries[random_number] == countries[83]:
        print("BOL_neutrality.tga")
    elif countries[random_number] == countries[84]:
        print("ECU_democratic.tga")
    elif countries[random_number] == countries[85]:
        print("PAR_communism.tga")
    elif countries[random_number] == countries[86]:
        print("flag")
    elif countries[random_number] == countries[87]:
        print("PRU_facsism.tga")
    elif countries[random_number] == countries[88]:
        print("URG.tga")
    elif countries[random_number] == countries[89]:
        print("VEN_facsism.tga")
    else:
        print("Do nothing")
#TODO - Add country flags
