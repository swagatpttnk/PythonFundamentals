class ComprehensionsDictionary:
    def __init__(self):
        pass
    def demo_dictionary_comprehension(self):
        friends = ["Annie", "Sppt", "Gary", "Olam", "Robin", "Obama"]
        time_since_seen= [3,5,6,17,28,8]
        long_timers ={
            friends[i]:time_since_seen[i]
            for i in range(len(friends))
            if time_since_seen[i] > 10
        }
        print(f"long_timers:{long_timers}")

        """ ======== Zip function ======= 
        Zip function packs the element of the multiple list.
        """
        long_timers = dict( zip(friends,time_since_seen) )
        long_timers={
             k:v
             for k,v in long_timers.items()
             if v>10
         }
        print(f"long_timers:{long_timers}")

        """ ======== Zip function with list etc ======= 
        If the list are of different , it zips till the len of smallest list.
        friends = ["Annie", "Sppt", "Gary", "Olam", "Robin", "Obama"]
        time_since_seen= [3,5,6,17,28,8]
        """
        origin = ["Norway","India","UnitedStates","China","Japan","New Zealand","Australia","South Africa","Venezuala"]
        long_timers = list( zip(friends,origin,time_since_seen) )
        print(f"long_timers with Origin:{long_timers}")

