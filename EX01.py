from IR import *


def main():
    print("Initializing the engine...")
    ir_engine = IR()
    
    print("Creating the inverted index")
    ir_engine.build_inverted_index()
    
    print("searching intersections for terms: 'president of the united states' and 'cost'")
    result = ir_engine.intersection("president of the united states", "cost")
    
    if not result:
        print("No itersection found:")
    else:
        print("found intersection in the following indexes: %s" % (",".join([str(index) for index in result])))
    
    print("Getting the text for index 21 (printing only 50 chars)")

    text = ir_engine.get_text_from_index(21)
    print(text[:50])
    
   # not printing the following lines beacuse they are pretty simillar with the previous example
    result = ir_engine.intersection("Russia", "Stakeholder")
       
    ir_engine.get_text_from_index(100)

    ir_engine.intersection("Russia", "usa")
    ir_engine.intersection("Russia", "united states of america")


main()


