from django.db import models

class Farmer(models.Model):
	phone = models.IntegerField(null=False)
	name = models.CharField(max_length=150)
	language = models.CharField(max_length=150)
	
	def __str__(self):
		return '%s' %(self.name)

class Farm(models.Model):
	area = models.IntegerField(null=False)
	village = models.CharField(max_length=150)
	crop = models.CharField(max_length=150)
	sowing_date = models.DateField()
	farmer = models.ForeignKey(Farmer)

	def __str__(self):
		return self.crop

class Schedulling(models.Model):
	days_from_sowing = models.IntegerField(null=False)
	fertilizer = models.CharField(max_length=150)
	quantity = models.IntegerField()
	quantity_unit = models.CharField(max_length=150)
	farm = models.ForeignKey(Farm)

	def __str__(self):
		return self.fertilizer

	# class Meta:
	# 	ordering=["farmer"]
		


#Django 
# Model the following data 
# -> Farmer data > Phone number, Name, Language 
# -> Farm data > Area, Village, Crop grown, Sowing date 
# -> Schedule data > Days after sowing, Fertiliser, Quantity, Quantity unit(ton, kg, g for solids and L, mL for liquids) 

# Views needed 
# -> Find all schedules due for today / tomorrow 
# -> Find all farmers who are growing a crop 
# -> Given prices of fertilisers, calculate the bill of materials for a single farmer 

# Note: 
# There is a 'sowing date' parameter in farm which defines when sowing was done. 
# A farm will have multiple schedules and they have a parameter called 'days from sowing' which define how many days the schedule is followed after sowing. 
# We want to know when a schedule is due, given by 'sowing date' + 'days from sowing' 


