# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NPTMTAkCR_p4HWRPCu15gIzLBYzRdjhX

**Task 06: Modifying RDF(s)**
"""

#pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
#g.parse(github_storage+"/rdf/example5.rdf", format="xml")
g.parse("../course_materials/rdf/example6.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University"**

"""

g.add((ns.University, RDF.type, RDFS.Class))

print("TASK 6.1")
for s, p, o in g.triples((None, RDF.type, RDFS.Class)):
  print(s)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

g.add((ns.Researcher, RDFS.subClassOf, ns.Person))

print("TASK 6.2")
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

g.add((ns.JaneSmith,RDF.type,ns.Researcher))

print("TASK 6.3")
for s, p, o in g.triples((None, RDF.type, ns.Researcher)):
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**"""

vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
g.add((ns.JaneSmith, vcard.FN, Literal("JaneSmith")))
g.add((ns.JaneSmith, vcard.Given, Literal("Jane")))
g.add((ns.JaneSmith, vcard.Family, Literal("Smith")))

print("TASK 6.4")
for s, p, o in g.triples((ns.JaneSmith, None, None)):
  print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

ns = Namespace("http://somewhere#")
g.add((ns.UPM, RDF.type, ns.University))
g.add((ns.JohnSmith, ns.work, ns.UPM))

print("TASK 6.5")
for s, p, o in g.triples((ns.JohnSmith, ns.work, None)):
  print(s,p,o)
  for s1, p1, o1 in g.triples((o, None, None)):
    print(s1, p1, o1)