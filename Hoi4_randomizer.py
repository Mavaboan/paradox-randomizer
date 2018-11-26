from __future__ import print_function
import random
from PIL import Image
import sys, os

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
random_number = random.randint(0,0)

#Prints a text telling user which country 
#Will be deleted later on when GUI is finished
print("Your country is gonna be")

#Prints the name of a country from the list, based on the randm number

print(countries[random_number])
print(random_number)

def country_flag():
    if countries[random_number] == countries[0]:
        land = "Flags\Relevant_flags\DEN_democratic.tga"
    elif countries[random_number] == countries[1]:
        land = ("Flags\Relevant_flags\\NOR_democratic.tga")
    elif countries[random_number] == countries[2]:
        land = ("Flags\Relevant_flags\FIN_neutrality.tga")
    elif countries[random_number] == countries[3]:
        land = ("Flags\Relevant_flags\ENG_democratic.tga")
    elif countries[random_number] == countries[4]:
        land = ("Flags\Relevant_flags\AMERICA_democratic.tga")
    elif countries[random_number] == countries[5]:
        land = ("Flags\Relevant_flags\SOV_communism.tga")
    elif countries[random_number] == countries[6]:
        land = ("Flags\Relevant_flags\POL_neutrality.tga")
    elif countries[random_number] == countries[7]:
        land = ("Flags\Relevant_flags\IRE_democratic.tga")
    elif countries[random_number] == countries[8]:
        land = ("Flags\Relevant_flags\SWE_democratic.tga")
    elif countries[random_number] == countries[9]:
        land = ("Flags\Relevant_flags\GER_facsism.tga")
    elif countries[random_number] == countries[10]:
        land = ("Flags\Relevant_flags\FRA_democratic.tga")
    elif countries[random_number] == countries[11]:
        land = ("Flags\Relevant_flags\SPR_democratic.tga")
    elif countries[random_number] == countries[12]:
        land = ("Flags\Relevant_flags\ITA_facsism.tga")
    elif countries[random_number] == countries[13]:
        land = ("Flags\Relevant_flags\JAP_facsism.tga")
    elif countries[random_number] == countries[14]:
        land = ("Flags\Relevant_flags\LIT_neutrality.tga")
    elif countries[random_number] == countries[15]:
        land = ("Flags\Relevant_flags\EST_neutrality.tga")
    elif countries[random_number] == countries[16]:
        land = ("Flags\Relevant_flags\LAT_neutrality.tga")
    elif countries[random_number] == countries[17]:
        land = ("Flags\Relevant_flags\ROM_neutrality.tga")
    elif countries[random_number] == countries[18]:
        land = ("Flags\Relevant_flags\YUG_neutrality.tga")
    elif countries[random_number] == countries[19]:
        land = ("Flags\Relevant_flags\GRE_neutrality.tga")
    elif countries[random_number] == countries[20]:
        land = ("Flags\Relevant_flags\ALB_neutrality.tga")
    elif countries[random_number] == countries[21]:
        land = ("Flags\Relevant_flags\BUL_neutrality.tga")
    elif countries[random_number] == countries[22]:
        land = ("Flags\Relevant_flags\HUN_facsism.tga")
    elif countries[random_number] == countries[23]:
        land = ("Flags\Relevant_flags\SLO_facsism.tga")
    elif countries[random_number] == countries[24]:
        land = ("Flags\Relevant_flags\LUX_democratic.tga")
    elif countries[random_number] == countries[25]:
        land = ("Flags\Relevant_flags\HOL_democratic.tga")
    elif countries[random_number] == countries[26]:
        land = ("Flags\Relevant_flags\CZE_democratic.tga")
    elif countries[random_number] == countries[27]:
        land = ("Flags\Relevant_flags\AUS_neutrality.tga")
    elif countries[random_number] == countries[28]:
        land = ("Flags\Relevant_flags\POR_neutrality.tga")
    elif countries[random_number] == countries[29]:
        land = ("Flags\Relevant_flags\SWI_democratic.tga")
    elif countries[random_number] == countries[30]:
        land = ("Flags\Relevant_flags\AFG_neutrality.tga")
    elif countries[random_number] == countries[31]:
        land = ("Flags\Relevant_flags\IRQ_neutrality.tga")
    elif countries[random_number] == countries[32]:
        land = ("Flags\Relevant_flags\OMA_neutrality.tga")
    elif countries[random_number] == countries[33]:
        land = ("Flags\Relevant_flags\PER_neutrality.tga")
    elif countries[random_number] == countries[34]:
        land = ("Flags\Relevant_flags\SAU_neutrality.tga")
    elif countries[random_number] == countries[35]:
        land = ("Flags\Relevant_flags\TUR_neutrality.tga")
    elif countries[random_number] == countries[36]:
        land = ("Flags\Relevant_flags\YEM_neutrality.tga")
    elif countries[random_number] == countries[37]:
        land = ("Flags\Relevant_flags\PHI_democratic.tga")
    elif countries[random_number] == countries[38]:
        land = ("Flags\Relevant_flags\SIA_facsism.tga")
    elif countries[random_number] == countries[39]:
        land = ("Flags\Relevant_flags\GXC_neutrality.tga")
    elif countries[random_number] == countries[40]:
        land = ("Flags\Relevant_flags\AST_democratic.tga")
    elif countries[random_number] == countries[41]:
        land = ("Flags\Relevant_flags\\NZL_democratic.tga")
    elif countries[random_number] == countries[42]:
        land = ("Flags\Relevant_flags\BHU_neutrality.tga")
    elif countries[random_number] == countries[43]:
        land = ("Flags\Relevant_flags\TIB_neutrality.tga")
    elif countries[random_number] == countries[44]:
        land = ("Flags\Relevant_flags\\NEP_neutrality.tga")
    elif countries[random_number] == countries[45]:
        land = ("Flags\Relevant_flags\RAJ_neutrality.tga")
    elif countries[random_number] == countries[46]:
        land = ("Flags\Relevant_flags\MEN_facsism.tga")
    elif countries[random_number] == countries[47]:
        land = ("Flags\Relevant_flags\SIA_neutrality.tga")
    elif countries[random_number] == countries[48]:
        land = ("Flags\Relevant_flags\CHI_neutrality.tga")
    elif countries[random_number] == countries[49]:
        land = ("Flags\Relevant_flags\LIB_democratic.tga")
    elif countries[random_number] == countries[50]:
        land = ("Flags\Relevant_flags\PRC_communism.tga")
    elif countries[random_number] == countries[51]:
        land = ("Flags\Relevant_flags\SHX_neutrality.tga")
    elif countries[random_number] == countries[52]:
        land = ("Flags\Relevant_flags\XSM_neutrality.tga")
    elif countries[random_number] == countries[53]:
        land = ("Flags\Relevant_flags\SIK_communism.tga")
    elif countries[random_number] == countries[54]:
        land = ("Flags\Relevant_flags\YUN_neutrality.tga")
    elif countries[random_number] == countries[55]:
        land = ("Flags\Relevant_flags\MON_communism.tga")
    elif countries[random_number] == countries[56]:
        land = ("Flags\Relevant_flags\TAN_communism.tga")
    elif countries[random_number] == countries[57]:
        land = ("Flags\Relevant_flags\ETH_neutrality.tga")
    elif countries[random_number] == countries[58]:
        land = ("Flags\Relevant_flags\SAF_democratic.tga")
    elif countries[random_number] == countries[59]:
        land = ("Flags\Relevant_flags\CAN_democratic.tga")
    elif countries[random_number] == countries[60]:
        land = ("Flags\Relevant_flags\MEX_neutrality.tga")
    elif countries[random_number] == countries[61]:
        land = ("Flags\Relevant_flags\COS_democratic.tga")
    elif countries[random_number] == countries[62]:
        land = ("Flags\Relevant_flags\ELS_facsism.tga")
    elif countries[random_number] == countries[63]:
        land = ("Flags\Relevant_flags\GUA__neutrality.tga")
    elif countries[random_number] == countries[64]:
        land = ("Flags\Relevant_flags\HON_democratic.tga")
    elif countries[random_number] == countries[65]:
        land = ("Flags\Relevant_flags\\NIC_democratic.tga")
    elif countries[random_number] == countries[66]:
        land = ("Flags\Relevant_flags\PAN_democratic.tga")
    elif countries[random_number] == countries[67]:
        land = ("Flags\Relevant_flags\CUB_democratic.tga")
    elif countries[random_number] == countries[68]:
        land = ("Flags\Relevant_flags\DOM_facsism.tga")
    elif countries[random_number] == countries[69]:
        land = ("Flags\Relevant_flags\HAI_democratic.tga")
    elif countries[random_number] == countries[70]:
        land = ("Flags\Relevant_flags\BRA_neutrality.tga")
    elif countries[random_number] == countries[71]:
        land = ("Flags\Relevant_flags\ARG_neutrality.tga")
    elif countries[random_number] == countries[72]:
        land = ("Flags\Relevant_flags\CHL_democratic.tga")
    elif countries[random_number] == countries[73]:
        land = ("Flags\Relevant_flags\COL_democratic.tga")
    elif countries[random_number] == countries[74]:
        land = ("Flags\Relevant_flags\BOL_neutrality.tga")
    elif countries[random_number] == countries[75]:
        land = ("Flags\Relevant_flags\ECU_democratic.tga")
    elif countries[random_number] == countries[76]:
        land = ("Flags\Relevant_flags\PAR_communism.tga")
    elif countries[random_number] == countries[77]:
        land = ("Flags\Relevant_flags\PRU_facsism.tga")
    elif countries[random_number] == countries[78]:
        land = "Flags\Relevant_flags\YKR.tga"
    elif countries[random_number] == countries[79]:
        land = "Flags\Relevant_flags\VEN_facsism.tga"
    else:
        print("Do nothing")
#TODO - Add country flags

print(country_flag())

#Shows an image of your country's flag - currently always shows Denmark

#Opens the Denmark flag .tga file
im = Image.open(land)


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
