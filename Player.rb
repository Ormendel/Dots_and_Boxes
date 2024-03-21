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
puts "total players playing: #{players.length()}"
for player in players do
    puts "Player: name = #{player.getName()}, Stamp = #{player.getLetter()}"
end