class Player
    def initialize(name)
       @name = name
       @letter = name[0].upcase()
    end
    def getName()
        return @name
    end
    def getLetter()
        return @letter
    end
 end

 # new - key word that calls to initialize function of the class
players = []
players.push(Player.new('or'))
players.push(Player.new('tom'))
n = players.length()
puts "total players playing: #{n}"
# for each loop
for i in 0..n-1 do # a..b --> [a,b]
    puts "Player ##{i+1}: name = #{players[i].getName()}, Stamp = #{players[i].getLetter()}"
end