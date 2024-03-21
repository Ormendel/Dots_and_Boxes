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
total_players = players.length()
puts "total players playing: #{total_players}"
for i in 0..total_players do
    puts "Player # #{i+1}: name = #{players[i].getName()}, Stamp = #{players[i].getLetter()}"
end