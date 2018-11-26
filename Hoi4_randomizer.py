from __future__ import print_function
import random
from PIL import Image
import os, sys

#All countries added!!
#The different countrys numbers added automaticly and starts with 0
countries = [
    "Denmark", "Norway", "Finland", "UK", "USA", "Soviet Union", 
    "Poland",  "Ireland", "Sweden", "Germany", "France", #10
    "Spain", "Italy", "Japan", "Lithuania", 
    "Estonia", "Latvia", "Romania", "Yugoslavia", #20
    "Greece", "Albania", "Bulgaria", "Hungary", 
    "Luxemborg", "Belgium", "Netherlands", "Czechoslovakia", #30
    "Austria", "Portugal", "Switzerland", "Afghanistan", "Iraq", 
    "Oman", "Iran", "Saudi Arabia", "Turkey", "Yemen", #40 
    "Australia", "New Zealand", "Bhutan", "Tibet", "Nepal", #50
    "British Raj", "Philipines", "Siam", "China", "Guangxi Clique", 
    "Peoples Republic of China", "Shanxi", "Xibei San Ma", "Sinkian", "Yunnan", #60
    "Mongolia", "Mengkukuo", "Tannu Tuva", "Liberia", 
    "Ethiopia", "South Africa", "Canada", "Mexico", "Costa Rica", #70
    "El Salvadore", "Guatamala", "Honduras", "Nicaragua", "Panama", 
    "Cuba", "Dominican Republic", "Haiti", "Brazil", "Argentina", #80
    "Chile", "Colombia", "Bolivia", "Ecuador", "Paraguay", 
    "Peru", "Uruguay", "Venezuela"
]

#!! Need to hardcode the country flags into the code !!

#Finds out how many countries there are

country_amount = len(countries)
#Finds a random number between 0 and the amount of countries we have.
random_number = random.randint(0,country_amount)

#Prints a text telling user which country 
#Will be deleted later on when GUI is finished
print("Your country is gonna be")

#Prints the name of a country from the list, based on the randm number

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
        print("LIT_neutrality.tga")
    elif countries[random_number] == countries[15]:
        print("EST_neutrality.tga")
    elif countries[random_number] == countries[16]:
        print("LAT_neutrality.tga")
    elif countries[random_number] == countries[17]:
        print("ROM_neutrality.tga")
    elif countries[random_number] == countries[18]:
        print("YUG_neutrality.tga")
    elif countries[random_number] == countries[19]:
        print("GRE_neutrality.tga")
    elif countries[random_number] == countries[20]:
        print("ALB_neutrality.tga")
    elif countries[random_number] == countries[21]:
        print("BUL_neutrality.tga")
    elif countries[random_number] == countries[22]:
        print("HUN_facsism.tga")
    elif countries[random_number] == countries[23]:
        print("SLO_facsism.tga")
    elif countries[random_number] == countries[24]:
        print("LUX_democratic.tga")
    elif countries[random_number] == countries[25]:
        print("HOL_democratic.tga")
    elif countries[random_number] == countries[26]:
        print("CZE_democratic.tga")
    elif countries[random_number] == countries[27]:
        print("AUS_neutrality.tga")
    elif countries[random_number] == countries[28]:
        print("POR_neutrality.tga")
    elif countries[random_number] == countries[29]:
        print("SWI_democratic.tga")
    elif countries[random_number] == countries[30]:
        print("AFG_neutrality.tga")
    elif countries[random_number] == countries[31]:
        print("IRQ_neutrality.tga")
    elif countries[random_number] == countries[32]:
        print("OMA_neutrality.tga")
    elif countries[random_number] == countries[33]:
        print("PER_neutrality.tga")
    elif countries[random_number] == countries[34]:
        print("SAU_neutrality.tga")
    elif countries[random_number] == countries[35]:
        print("TUR_neutrality.tga")
    elif countries[random_number] == countries[36]:
        print("YEM_neutrality.tga")
    elif countries[random_number] == countries[37]:
        print("PHI_democratic.tga")
    elif countries[random_number] == countries[38]:
        print("SIA_facsism.tga")
    elif countries[random_number] == countries[39]:
        print("GXC_neutrality.tga")
    elif countries[random_number] == countries[40]:
        print("AST_democratic.tga")
    elif countries[random_number] == countries[41]:
        print("NZL_democratic.tga")
    elif countries[random_number] == countries[42]:
        print("BHU_neutrality.tga")
    elif countries[random_number] == countries[43]:
        print("TIB_neutrality.tga")
    elif countries[random_number] == countries[44]:
        print("NEP_neutrality.tga")
    elif countries[random_number] == countries[45]:
        print("RAJ_neutrality.tga")
    elif countries[random_number] == countries[46]:
        print("MEN_facsism.tga")
    elif countries[random_number] == countries[47]:
        print("SIA_neutrality.tga")
    elif countries[random_number] == countries[48]:
        print("CHI_neutrality.tga")
    elif countries[random_number] == countries[49]:
        print("LIB_democratic.tga")
    elif countries[random_number] == countries[50]:
        print("PRC_communism.tga")
    elif countries[random_number] == countries[51]:
        print("SHX_neutrality.tga")
    elif countries[random_number] == countries[52]:
        print("XSM_neutrality.tga")
    elif countries[random_number] == countries[53]:
        print("SIK_communism.tga")
    elif countries[random_number] == countries[54]:
        print("YUN_neutrality.tga")
    elif countries[random_number] == countries[55]:
        print("MON_communism.tga")
    elif countries[random_number] == countries[56]:
        print("TAN_communism.tga")
    elif countries[random_number] == countries[57]:
        print("ETH_neutrality.tga")
    elif countries[random_number] == countries[58]:
        print("SAF_democratic.tga")
    elif countries[random_number] == countries[59]:
        print("CAN_democratic.tga")
    elif countries[random_number] == countries[60]:
        print("MEX_neutrality.tga")
    elif countries[random_number] == countries[61]:
        print("COS_democratic.tga")
    elif countries[random_number] == countries[62]:
        print("ELS_facsism.tga")
    elif countries[random_number] == countries[63]:
        print("GUA__neutrality.tga")
    elif countries[random_number] == countries[64]:
        print("HON_democratic.tga")
    elif countries[random_number] == countries[65]:
        print("NIC_democratic.tga")
    elif countries[random_number] == countries[66]:
        print("PAN_democratic.tga")
    elif countries[random_number] == countries[67]:
        print("CUB_democratic.tga")
    elif countries[random_number] == countries[68]:
        print("DOM_facsism.tga")
    elif countries[random_number] == countries[69]:
        print("HAI_democratic.tga")
    elif countries[random_number] == countries[70]:
        print("BRA_neutrality.tga")
    elif countries[random_number] == countries[71]:
        print("ARG_neutrality.tga")
    elif countries[random_number] == countries[72]:
        print("CHL_democratic.tga")
    elif countries[random_number] == countries[73]:
        print("COL_democratic.tga")
    elif countries[random_number] == countries[74]:
        print("BOL_neutrality.tga")
    elif countries[random_number] == countries[75]:
        print("ECU_democratic.tga")
    elif countries[random_number] == countries[76]:
        print("PAR_communism.tga")
    elif countries[random_number] == countries[77]:
        print("PRU_facsism.tga")
    elif countries[random_number] == countries[78]:
        print("URG.tga")
    elif countries[random_number] == countries[79]:
        print("VEN_facsism.tga")
    else:
        print("Do nothing")
#TODO - Add country flags


#Shows an image of your country's flag - currently always shows Denmark

#Opens the Denmark flag .tga file
im = Image.open(country_flag)

#If you stare into the abyss, the abyss stares back
#Converts the .tga file to a .jpg
for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        #If a mistake happens, gives an error message
        except IOError:
            print("cannot convert", infile)
#Shows the .jpg file
im.show()
