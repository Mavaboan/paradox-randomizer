#Imports.
from __future__ import print_function
import random
from PIL import Image
import sys, os
#The different countries numbers added automaticly and starts with 0.
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
#Finds out how many countries there are.
country_amount = len(countries)
#Finds a random number between 0 and the amount of countries we have.
random_number = random.randint(0,country_amount)

#Prints a text telling user which country.
#Will be deleted later on when GUI is finished.
print("Your country is gonna be")

#Prints the name of a country from the list, and the foun number, based on the random number.

print(countries[random_number])
print(random_number)

#Finds the flag of the selected country.
def country_flag():
    if countries[random_number] == countries[0]:

        return "Flags\Relevant_flags\DEN_democratic.tga"
    elif countries[random_number] == countries[1]:
        return ("Flags\Relevant_flags\\NOR_democratic.tga")
    elif countries[random_number] == countries[2]:
        return ("Flags\Relevant_flags\FIN_neutrality.tga")
    elif countries[random_number] == countries[3]:
        return ("Flags\Relevant_flags\ENG_democratic.tga")
    elif countries[random_number] == countries[4]:
        return ("Flags\Relevant_flags\AMERICA_democratic.tga")
    elif countries[random_number] == countries[5]:
        return ("Flags\Relevant_flags\SOV_communism.tga")
    elif countries[random_number] == countries[6]:
        return ("Flags\Relevant_flags\POL_neutrality.tga")
    elif countries[random_number] == countries[7]:
        return ("Flags\Relevant_flags\IRE_democratic.tga")
    elif countries[random_number] == countries[8]:
        return ("Flags\Relevant_flags\SWE_democratic.tga")
    elif countries[random_number] == countries[9]:
        return ("Flags\Relevant_flags\GER_fascism.tga")
    elif countries[random_number] == countries[10]:
        return ("Flags\Relevant_flags\FRA_democratic.tga")
    elif countries[random_number] == countries[11]:
        return ("Flags\Relevant_flags\SPR_democratic.tga")
    elif countries[random_number] == countries[12]:
        return ("Flags\Relevant_flags\ITA_fascism.tga")
    elif countries[random_number] == countries[13]:
        return ("Flags\Relevant_flags\JAP_fascism.tga")
    elif countries[random_number] == countries[14]:
        return ("Flags\Relevant_flags\LIT_neutrality.tga")
    elif countries[random_number] == countries[15]:
        return ("Flags\Relevant_flags\EST_neutrality.tga")
    elif countries[random_number] == countries[16]:
        return ("Flags\Relevant_flags\LAT_neutrality.tga")
    elif countries[random_number] == countries[17]:
        return ("Flags\Relevant_flags\ROM_neutrality.tga")
    elif countries[random_number] == countries[18]:
        return ("Flags\Relevant_flags\YUG_neutrality.tga")
    elif countries[random_number] == countries[19]:
        return ("Flags\Relevant_flags\GRE_neutrality.tga")
    elif countries[random_number] == countries[20]:
        return ("Flags\Relevant_flags\ALB_neutrality.tga")
    elif countries[random_number] == countries[21]:
        return ("Flags\Relevant_flags\BUL_neutrality.tga")
    elif countries[random_number] == countries[22]:
        return ("Flags\Relevant_flags\HUN_fascism.tga")
    elif countries[random_number] == countries[23]:
        return ("Flags\Relevant_flags\SLO_fascism.tga")
    elif countries[random_number] == countries[24]:
        return ("Flags\Relevant_flags\LUX_democratic.tga")
    elif countries[random_number] == countries[25]:
        return ("Flags\Relevant_flags\HOL_democratic.tga")
    elif countries[random_number] == countries[26]:
        return ("Flags\Relevant_flags\CZE_democratic.tga")
    elif countries[random_number] == countries[27]:
        return ("Flags\Relevant_flags\AUS_neutrality.tga")
    elif countries[random_number] == countries[28]:
        return ("Flags\Relevant_flags\POR_neutrality.tga")
    elif countries[random_number] == countries[29]:
        return ("Flags\Relevant_flags\SWI_democratic.tga")
    elif countries[random_number] == countries[30]:
        return ("Flags\Relevant_flags\AFG_neutrality.tga")
    elif countries[random_number] == countries[31]:
        return ("Flags\Relevant_flags\IRQ_neutrality.tga")
    elif countries[random_number] == countries[32]:
        return ("Flags\Relevant_flags\OMA_neutrality.tga")
    elif countries[random_number] == countries[33]:
        return ("Flags\Relevant_flags\PER_neutrality.tga")
    elif countries[random_number] == countries[34]:
        return ("Flags\Relevant_flags\SAU_neutrality.tga")
    elif countries[random_number] == countries[35]:
        return ("Flags\Relevant_flags\TUR_neutrality.tga")
    elif countries[random_number] == countries[36]:
        return ("Flags\Relevant_flags\YEM_neutrality.tga")
    elif countries[random_number] == countries[37]:
        return ("Flags\Relevant_flags\AUS_democratic.tga")
    elif countries[random_number] == countries[38]:
        return ("Flags\Relevant_flags\\NZL_democratic.tga")
    elif countries[random_number] == countries[39]:
        return ("Flags\Relevant_flags\BHU_neutrality.tga")
    elif countries[random_number] == countries[40]:
        return ("Flags\Relevant_flags\TIB_neutrality.tga")
    elif countries[random_number] == countries[41]:
        return ("Flags\Relevant_flags\\NEP_neutrality.tga")
    elif countries[random_number] == countries[42]:
        return ("Flags\Relevant_flags\RAJ_neutrality.tga")
    elif countries[random_number] == countries[43]:
        return ("Flags\Relevant_flags\PHI_democratic.tga")
    elif countries[random_number] == countries[44]:
        return ("Flags\Relevant_flags\SIA_neutrality.tga")
    elif countries[random_number] == countries[45]:
        return ("Flags\Relevant_flags\CHI_neutrality.tga")
    elif countries[random_number] == countries[46]:
        return ("Flags\Relevant_flags\GXC_neutrality.tga")
    elif countries[random_number] == countries[47]:
        return ("Flags\Relevant_flags\PRC_communism.tga")
    elif countries[random_number] == countries[48]:
        return ("Flags\Relevant_flags\SHX_neutrality.tga")
    elif countries[random_number] == countries[49]:
        return ("Flags\Relevant_flags\XSM_neutrality.tga")
    elif countries[random_number] == countries[50]:
        return ("Flags\Relevant_flags\SIK_communism.tga")
    elif countries[random_number] == countries[51]:
        return ("Flags\Relevant_flags\YUN_neutrality.tga")
    elif countries[random_number] == countries[52]:
        return ("Flags\Relevant_flags\MON_communism.tga")
    elif countries[random_number] == countries[53]:
        return ("Flags\Relevant_flags\MEN.tga")
    elif countries[random_number] == countries[54]:
        return ("Flags\Relevant_flags\TAN_communism.tga")
    elif countries[random_number] == countries[55]:
        return ("Flags\Relevant_flags\LIB_democratic.tga")
    elif countries[random_number] == countries[56]:
        return ("Flags\Relevant_flags\ETH_neutrality.tga")
    elif countries[random_number] == countries[57]:
        return ("Flags\Relevant_flags\SAF_democratic.tga")
    elif countries[random_number] == countries[58]:
        return ("Flags\Relevant_flags\CAN_democratic.tga")
    elif countries[random_number] == countries[59]:
        return ("Flags\Relevant_flags\MEX_neutrality.tga")
    elif countries[random_number] == countries[60]:
        return ("Flags\Relevant_flags\COS_democratic.tga")
    elif countries[random_number] == countries[61]:
        return ("Flags\Relevant_flags\ELS_fascism.tga")
    elif countries[random_number] == countries[62]:
        return ("Flags\Relevant_flags\GUA__neutrality.tga")
    elif countries[random_number] == countries[63]:
        return ("Flags\Relevant_flags\HON_democratic.tga")
    elif countries[random_number] == countries[64]:
        return ("Flags\Relevant_flags\\NIC_neutrality.tga")
    elif countries[random_number] == countries[65]:
        return ("Flags\Relevant_flags\PAN_democratic.tga")
    elif countries[random_number] == countries[66]:
        return ("Flags\Relevant_flags\CUB_democratic.tga")
    elif countries[random_number] == countries[67]:
        return ("Flags\Relevant_flags\DOM_fascism.tga")
    elif countries[random_number] == countries[68]:
        return ("Flags\Relevant_flags\HAI_democratic.tga")
    elif countries[random_number] == countries[69]:
        return ("Flags\Relevant_flags\BRA_neutrality.tga")
    elif countries[random_number] == countries[70]:
        return ("Flags\Relevant_flags\ARG_neutrality.tga")
    elif countries[random_number] == countries[71]:
        return ("Flags\Relevant_flags\CHL_democratic.tga")
    elif countries[random_number] == countries[72]:
        return ("Flags\Relevant_flags\COL_democratic.tga")
    elif countries[random_number] == countries[73]:
        return ("Flags\Relevant_flags\BOL_neutrality.tga")
    elif countries[random_number] == countries[74]:
        return ("Flags\Relevant_flags\ECU_democratic.tga")
    elif countries[random_number] == countries[75]:
        return ("Flags\Relevant_flags\PAR_communism.tga")
    elif countries[random_number] == countries[76]:
        return ("Flags\Relevant_flags\PRU_fascism.tga")
    elif countries[random_number] == countries[77]:
        return ("Flags\Relevant_flags\YKR.tga")
    elif countries[random_number] == countries[78]:
        return "Flags\Relevant_flags\VEN_fascism.tga"
    else:
        print("can't find flag")

#Opens the image of the flag .tga file.
im = Image.open(country_flag())

#If you stare into the abyss, the abyss stares back.
#Converts the .tga file to a .jpg

#Sets up a for loop with the variable "infile"(which is the file we want to make a jpg.) in system arguments.
for infile in sys.argv[1:]:
    #Splits the "infile" in two parts, a root and an ext. Then makes "f" the root and "e" the ext.
    f, e = os.path.splitext(infile)
    #Defines outfile as "f" plus ".jpg"
    outfile = f + ".jpg"
    #Checks if the "infile" is the same as the "outfile"
    if infile != outfile:
        #Saves the .tga as a .jpg
        try:
            Image.open(infile).save(outfile)
        #If a mistake happens, gives an error message.
        except IOError:
            print("cannot convert", infile)
#Shows the saved .jpg file.
im.show()
