import pandas as pd
import csv 

Age =  ["30-40", "40-50", "50-60"]
Gender =  ["Male", "Female"]
Sector  = ["Public", "Private"]
workingsamesector  = ["Below 5 years", "Above 5 years"]
Specialization =  ["Counselor", "Anesthetic", "Casualty medical officer", "Critical Care Medicine", "Fetal medicine", 
"General Practitioner", "Gynaecology", "Neurology", "Paediatrics", "Pathology0", "Radiologist1", "Surgeon2"]
Work_hours  = ["5hrs", "10hrs", "More than 10hrs"]
Workyearsspan  = ["Below 5 years", "Between 5 to 10 years", "Above 10 Years"]
Patientperday  = ["Below 10", "Between 10-20", "Between 20-30", "Above 30"]
Overtimeworkinterest  = ["Yes", "No"]
Overtimeworkpaid  = ["Yes", "No"]
Stressedduringwork  = ["Sometimes", "Very Often", "Never"]
Feelingonjob =  ["I am completely happy and enjoying the job", "I sometimes feel dissatisfied but generally enjoy my job", 
"Most of the time I do not enjoy my work", "I have no interest at all in my work"]
Sourceofstress  = ["Over work", "Family Issues", "Hospital Management", "Patitent Attitude", "All above in different proportions"]
Handling_stress  = ["Talking to an expert", "Taking a sleep", "Drugs / Alcohol / Smoking", "Talking to your family members", "Talking to the employer"]
InformManagementproblems  = ["Yes", "No"]
Managementinitiativeto_problems = ["Taken but was not effective", "Effective method was imposed", "No action was taken"]
Hospitalcaretowards_stress  = ["Counselling", "Rearranging the work timing", "Refreshments", "No care was given"]
Stressaffectingpatient_care  = [ "Yes", "No"]
Stressaffectingconcentration  = ["Very often", "Somewhat", "Never"]
Efforttoreducestresstoimproveconcentration = ["No effort", "Some effort", "Lot of effort"]
Stressduetotoomany_duties =  ["Yes", "No"]
Stressdueto_age =  ["Yes", "No"]
Stressreasonfamily  = ["Yes", "No"]
Stressdueto_competition  = ["Yes", "No"]
Prefertostay_alone =  ["Yes", "No"]
Prefertakingresponsibilities  = ["Yes", "No"]
Alcohol_usage =  ["Daily", "Occasionally", "Sometimes", "Never"]
Stressnervoushabits =  ["Daily", "Occasionally", "Sometimes", "Never"]
Stressmakesnervous  = ["Yes", "No"]
Stressaffectsemotions = ["Very often", "Somewhat", "Never"]

T = [Age, Gender, Sector, workingsamesector, Specialization, Work_hours,
	Workyearsspan, Patientperday, Overtimeworkinterest, Overtimeworkpaid, 
	Stressedduringwork, Feelingonjob, Sourceofstress, Handling_stress, InformManagementproblems,
	Managementinitiativeto_problems, Hospitalcaretowards_stress, Stressaffectingpatient_care, 
	Stressaffectingconcentration, Efforttoreducestresstoimproveconcentration, Stressduetotoomany_duties,
	Stressdueto_age, Stressreasonfamily, Stressdueto_competition, Prefertostay_alone, 
	Prefertakingresponsibilities, Alcohol_usage, Stressnervoushabits,
	Stressmakesnervous, Stressaffectsemotions]

df = pd.read_csv('./data.csv')

def get_number_of_practitionners():
	return len(df["Stressed_during_work"])

def print_attrib():
	for e, i in enumerate(df):
		print(e , " : " , i)

def get_attrib():
	return [i for i in df]

def copy_array(array):
	return [element for element in array]

def print_tab2D(t):
	for e in t:
		print(e)

def csv_to_array():
	t = []
	nb = get_number_of_practitionners()
	for i in range(nb):
		p = [df[attrib][i] for attrib in df]
		t.append(p)
	return t

def get_value_by_index(t, index, values):
	return [line for line in t if (line[index] in values)]

def get_nb_of_value_by_index(t, index, values):
	return sum((line[index] in values) for line in t)

def get_repetition(t,limit):
	m = []
	acc = []
	f = []
	s = ""
	for line in t:
		if (line not in m):
			m.append(line)
			acc.append(1)
		else:
			acc[m.index(line)] += 1
	for i in range(len(m)):
		if (acc[i] > 1):
			if (acc[i] > 100 and acc[i] < 1000):
				s+=" "
			elif (acc[i] < 100 and acc[i] > 10):
				s+="  "
			elif (acc[i] < 10):
				s+="   "
			#print(acc[i], s, " : ", m[i])
			#print(m[i])
			if (acc[i] >= limit):
				f.append(m[i])
		s=""
	return f

def get_similarity(t, r, ban):
	a = []
	b = []
	for attrib in range(len(T)):
		v = -1
		err = False
		if (attrib not in ban):
			rep = 0
			for tab in t:
				if (v == -1):
					v = tab[attrib]
				else:
					if (tab[attrib] != v):
						if (rep == r):
							err = True
							break
						rep += 1
			if (not err):
				a.append(attrib)
				b.append(tab[attrib])
	return a, b

def reform_data(t, ban):
	_t = copy_array(t)
	for e in range(len(T)):
		if (e in ban):
			_t[e] = 0
	return _t

def verification_de_la_donnée(A,lst_t,ban,typ):
	y = [0,0,0]
	for line in A:
		typ_line = line[10]
		l = reform_data(line,ban)
		for t in lst_t:
			v = reform_data(t,ban)
			if (l == v):
				y[typ_line-1] += 1
				break
	return y


def verification_de_la_données(A,lst_t,ban,typ):
	y = [0,0]
	for line in A:
		typ_line = line[10]
		l = reform_data(line,ban)
		for t in lst_t:
			v = reform_data(t,ban)
			if (l == v):
				if (typ_line == typ):
					y[0] += 1
				else:
					y[1] += 1
				break
	return y

def get_mask(A,lst_t,typ,limit):
	l = int(len(lst_t)/2)
	score = 0
	r = []

	if typ in [2, 1]:
		l += 1

	for i in range(l):
		a,b=get_similarity(lst_t,i,[10])
		a.append(10)
		res = verification_de_la_données(A,lst_t,a,typ)
		#if (res[(typ+1)%3] < limit and res[(typ+2)%3] < limit):
		if (res[1] < limit and res[0] > score):
			r = copy_array(a)
			score = res[0]
	return r

def get_reverse_mask(mask):
	return [e for e in range(len(T)) if (e not in mask)]

def get_facteur_by_typ(typ):
	l = 1100

	if (typ == 3): 
		l = 3000

	tableau_repetition = get_repetition(get_value_by_index(A,10,[typ]),l)
	mask = get_mask(A,tableau_repetition,typ,l)
	return get_reverse_mask(mask)

def get_number_of_type(data,typ):
	l = 1100

	if (typ == 3): 
		l = 3000

	tableau_repetition = get_repetition(get_value_by_index(A,10,[typ]),l)
	mask = get_mask(A,tableau_repetition,typ,l)

	return verification_de_la_données(A, tableau_repetition, mask, typ)[0]

# Nombre total de practitiens  	: 100 000
# Nombre de 'sometimes' stress 	: 53391
# Nombre de 'often' stress 		: 39947
# Nombre de 'never' stress 		: 6662

# Transformation du tableau en une autre forme (par preference)
#A = csv_to_array()

# Renvoi les facteurs qui influe sur le type 
#get_facteur_by_typ(1) # => [4, 5, 6, 7, 12, 13, 15, 26, 27]
#get_facteur_by_typ(2) # => [0, 3, 5, 6, 7, 11, 12, 13, 17, 19, 23]
#get_facteur_by_typ(3) # => [1, 4, 5, 6, 7, 12, 13, 16, 18, 20, 21, 26, 27, 29]

# Retourne le nombre de type t trouvé dans le jeu de données
#get_number_of_type(A,1) # => 52863 
#get_number_of_type(A,2) # => 38724
#get_number_of_type(A,3) # => 6662

# Retourne le mask qui permet de cibler le jeu de données en fonction du type
#get_mask(A,get_repetition(get_value_by_index(A,10,[3]),3000),3,3000) # => [0, 2, 3, 8, 9, 11, 14, 15, 17, 19, 22, 23, 24, 25, 28, 10]
#get_mask(A,get_repetition(get_value_by_index(A,10,[2]),1100),2,1100) # => [1, 2, 4, 8, 9, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 29, 10]
#get_mask(A,get_repetition(get_value_by_index(A,10,[1]),1100),1,1100) # => [0, 1, 2, 3, 8, 9, 11, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 28, 29, 10]








