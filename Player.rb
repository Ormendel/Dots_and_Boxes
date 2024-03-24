class Player
    attr_accessor :name, :letter
    def initialize(name)
       @name = name
       @letter = name[0].upcase()
    end

    #Overriding to_string method
    def to_s
        return "Name = #{name}, Stamp = #{letter}"
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
    puts "Player ##{i+1}: #{players[i]}"
end