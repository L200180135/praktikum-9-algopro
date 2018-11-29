# Kegiatan 1
a = open ("l200180135" , "w")
a.write ("L200180135" "\n")
a.write ("20-01-2000" "\n")
a.write ("Anisa Ghoyatul Firdaus" "\n")
a.write ("01-20-2000" "\n")
a.write ("Boyolali" "\n")

# Kegiatan 2
a = open ("l200180135" , "r")
nm = a.readline ()
ttl= a.readline ()
nme = a.readline ()
ttlmm = a.readline ()
asl = a.readline ()
a.close ()

a = open ("l200180135" , "w")
a.write (nme)
a.write (asl)
a.write (ttlmm)
a.write (nm)
a.close ()

# Kegiatan 3 dan 4
import shelve

a = open ("l200180135" , "r")
g = shelve.open ("nsa")
g ["Nama"] = a.readline ()
g ["Asal"] = a.readline () 
g ["TTL"] = a.readline ()
g ["NIM"] = a.readline ()
g.close ()
a.close ()


g = shelve.open ("nsa")
print g ["Nama"]
print g ["Asal"] , g ["TTL"]
print g ["NIM"]
g.close () 



