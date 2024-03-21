class Player
    @@no_players = 0
    def initialize(name)
       @name = name
       @letter = name[0].upcase()
       @@no_players += 1
    end
    def getName()
        return @name
     end
     def getLetter()
        return @letter
     end
     def self.variable
        return @@no_players # Return the value of this variable
     end
 end

player1 = Player.new('or') # It calls initialize function
player2 = Player.new('tom')

puts "total players playing: #{Player.variable}"
puts "Continue later"