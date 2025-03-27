def pest_control():
    a=input("enter the crop recommended by the experts")
    if a in("rice","Rice","RICE"):
        print('''For Rice:
              Pest name:
              (I)Rice stem borer:
              Early detection: Check for “ white heads “ in riceplants
              Control/Solution: Introduce beetle coccinellids or tricogramma wasps  which are natural predators of rice stem borer
              (II)Brown Planthopper:
              Early detection: Yellowing of rice plants and stunted growth
              Control/Solution : Use Imidacloprid or buprofezin pesticide
              (III)Whiteback planthopper:
              Early detection : Rice plants have a “ burnt “ appearance
              Control/Solution: Use pesticide Clothiandin
              (IV)Rice Gall midge:
              Early detection : A silver shoot appears in the rice plant
              Control/Solution : Use pesticide fipronil''')
    elif a in("wheat","WHEAT","Wheat"):
        print('''Wheat
Hessian fly:
Early detection: Darkened circles on leaves and the central shoot dies
Control/Solution: use pesticide thiamethoxam
Aphids:
Early detection : Spikes on leaves or stems
Control/Solution: use pesticide imidacloprid
Rust diseases :
Early detection: Rust colour on leaves
Control/Solution : Use fungi triazole''')
    elif a in ("maize","Maize","MAIZE"):
        print('''For maize:
Fall Armyworm :

Early Detection: Regularly scout maize fields for signs of fall armyworm damage, such as ragged leaf edges, windowpane feeding on leaves, or frass (insect excrement) on leaves.
Control Solutions: Apply insecticides targeted at fall armyworm larvae during early stages of infestation. Use biological control agents such as parasitoids (e.g., Trichogramma spp.) or predators (e.g., lady beetles) where feasible. Implement cultural practices such as early planting or intercropping with repellent crops.
Corn Earworm :

Early Detection: Monitor maize ears for signs of corn earworm damage, such as feeding holes and frass in the husks or silk channels.
Control Solutions: Apply insecticides targeted at corn earworm larvae during early ear development stages. Implement cultural practices such as pheromone trapping or planting early-maturing maize varieties to avoid peak corn earworm populations.
European Corn Borer :
Early Detection: Monitor maize stalks for signs of European corn borer damage, such as entry holes and frass near the base of plants.
Control Solutions: Apply insecticides targeted at European corn borer larvae during early larval stages. Implement cultural practices such as crop rotation or planting Bt (Bacillus thuringiensis) maize varieties with genetic resistance to corn borers.
Maize Weevil :

Early Detection: Inspect stored maize grains for signs of maize weevil infestation, such as damaged kernels, holes in grain, or the presence of adult weevils.
Control Solutions: Use grain protectants such as diatomaceous earth or insecticidal dusts to treat stored maize grains. Implement sanitation measures to remove spilled grain and reduce weevil breeding sites.
Stalk Borers :

Early Detection: Monitor maize stalks for signs of stalk borer damage, such as entry holes, frass, or wilting plants.
Control Solutions: Apply insecticides targeted at stalk borer larvae during early larval stages. Implement cultural practices such as timely planting or removing crop residues to reduce overwintering sites.
Wireworms:

Early Detection: Monitor maize fields for signs of wireworm damage, such as seedling wilting, tunneling in roots, or feeding scars on seeds.
Control Solutions: Use soil insecticides or seed treatments containing neonicotinoids or other effective active ingredients to protect maize seeds from wireworm damage. Implement cultural practices such as crop rotation or fallow periods to reduce wireworm populations.
        
''')
    elif a in("SUGAR CANE","Sugar Cane","sugar cane"):
        print('''For sugarcane:
Sugarcane Borer:

Detection: Monitor sugarcane stalks for signs of borer damage, such as entry holes, frass, or stalk breakage.
Control: Apply insecticides targeted at sugarcane borers during early larval stages. Implement cultural practices such as early planting, crop rotation, or planting borer-resistant sugarcane varieties.
Sugarcane Whitefly :

Detection: Inspect sugarcane leaves for signs of whitefly infestation, such as white nymphs on the undersides of leaves or sticky honeydew secretions.
Control: Apply insecticides targeted at sugarcane whiteflies during early infestation stages. Implement cultural practices such as maintaining proper field hygiene and promoting natural enemies such as parasitoids and predators.
Sugarcane Woolly Aphid:

Detection: Monitor sugarcane fields for signs of woolly aphid infestation, such as white waxy secretions on leaves and stems.
Control: Apply insecticides targeted at woolly aphids during early infestation stages. Implement cultural practices such as maintaining proper field hygiene and promoting natural enemies such as parasitoids and predators.

''')
    elif a in("ONION","Onion","onion"):
        print('''Onion Thrips :

Detection: Monitor onion foliage for signs of thrips damage, such as silvering, scarring, or distorted leaves. Use yellow sticky traps to monitor adult thrips populations.
Control: Apply insecticides targeted at thrips during early infestation stages. Implement cultural practices such as crop rotation, removing weed hosts, and planting thrips-resistant onion varieties. Biological control agents like predatory mites can also help manage thrips populations.
Onion Maggots :

Detection: Monitor onion seedlings for signs of maggot feeding damage on roots and bulbs, such as stunted growth, wilting, or yellowing. Use bait traps or sticky traps to monitor adult fly activity.
Control: Apply soil insecticides or seed treatments targeted at onion maggot larvae during early planting stages. Implement cultural practices such as crop rotation, delaying planting, or using floating row covers to protect seedlings from egg-laying flies. Biological control agents like entomopathogenic nematodes can also help manage maggot populations.
Onion Bulb Mites :

Detection: Inspect stored onion bulbs for signs of mite damage, such as feeding scars, tunnels, or mold growth. Use sticky traps or soil samples to monitor mite populations in the field.
Control: Use acaricides or insecticides targeted at mites during storage or field stages. Implement cultural practices such as proper sanitation, maintaining low humidity levels, and avoiding overcrowding during storage. Biological control agents like predatory mites can also help manage mite populations.
Onion Root Maggots :

Detection: Monitor onion roots for signs of maggot feeding damage, such as tunneling, discoloration, or rotting. Use bait traps or sticky traps to monitor adult fly activity.
Control: Apply soil insecticides or seed treatments targeted at onion maggot larvae during early planting stages. Implement cultural practices such as crop rotation, delaying planting, or using floating row covers to protect seedlings from egg-laying flies. Biological control agents like entomopathogenic nematodes can also help manage maggot populations.
Thrips and Aphids:

Detection: Monitor onion foliage for signs of thrips and aphid damage, such as feeding scars, distorted leaves, or honeydew secretion. Use yellow sticky traps to monitor adult thrips populations.
Control: Apply insecticides targeted at thrips and aphids during early infestation stages. Implement cultural practices such as removing weed hosts, maintaining weed-free field margins, and promoting natural enemies like predatory insects and parasitoids
''')
    elif a in("RAGI","Ragi","ragi"):
        print('''Armyworms :
Detection: Regularly scout ragi fields for signs of armyworm damage, such as ragged leaf edges, windowpane feeding on leaves, or frass (insect excrement) on leaves.
Control: Apply insecticides targeted at armyworm larvae during early infestation stages. Implement cultural practices such as maintaining proper field hygiene, promoting natural enemies such as parasitoids and predators, and timely planting to avoid peak armyworm populations.
Shoot Fly :

Detection: Monitor ragi plants for signs of shoot fly damage, such as "dead hearts" or stunted growth of shoot tips.
Control: Apply systemic insecticides or seed treatments targeted at shoot fly larvae during early crop growth stages. Implement cultural practices such as early planting, avoiding excess nitrogen fertilization, and using resistant ragi varieties where available.
Earhead Bug :

Detection: Inspect ragi earheads for signs of earhead bug damage, such as feeding scars, discoloration, or damaged grains.
Control: Apply insecticides targeted at earhead bugs during early grain development stages. Implement cultural practices such as maintaining proper field sanitation, promoting natural enemies such as predatory insects, and harvesting crops promptly to reduce bug populations.
Grasshoppers :

Detection: Monitor ragi fields for signs of grasshopper feeding damage, such as defoliation, clipped leaves, or damaged stems.
Control: Apply insecticides targeted at grasshoppers during early infestation stages. Implement cultural practices such as maintaining proper field hygiene, promoting natural enemies such as birds and predatory insects, and using physical barriers or traps to prevent grasshopper access to crops.
Leaf Spot and Blast Diseases:

Detection: Monitor ragi plants for signs of leaf spot and blast diseases, such as leaf lesions, premature leaf senescence, or fungal spores on leaves.
Control: Apply fungicides targeted at fungal pathogens during early disease development stages. Implement cultural practices such as crop rotation, avoiding excessive irrigation, promoting air circulation, and using disease-resistant ragi varieties where available.
''')
    elif a in ("JOWAR","Jowar","jowar"):
        print('''Detection: Monitor jowar plants for signs of shoot fly damage, such as "dead hearts" or stunted growth of shoot tips.
Control: Apply systemic insecticides or seed treatments targeted at shoot fly larvae during early crop growth stages. Implement cultural practices such as early planting, avoiding excess nitrogen fertilization, and using resistant jowar varieties where available.
Stem Borers :

Detection: Inspect jowar stems for signs of stem borer damage, such as entry holes, frass, or tunneling.
Control: Apply insecticides targeted at stem borer larvae during early infestation stages. Implement cultural practices such as crop rotation, avoiding excessive irrigation, and promoting natural enemies such as parasitoids and predators.
Sorghum Midge :

Detection: Monitor jowar panicles for signs of midge damage, such as discolored or damaged kernels.
Control: Apply insecticides targeted at midge larvae during early kernel development stages. Implement cultural practices such as timely planting, promoting natural enemies such as predatory insects, and using physical barriers to protect panicles from midge infestation.
Head Bugs :

Detection: Inspect jowar panicles for signs of head bug damage, such as feeding scars or damaged grains.
Control: Apply insecticides targeted at head bugs during early grain development stages. Implement cultural practices such as maintaining proper field sanitation, promoting natural enemies such as predatory insects, and harvesting crops promptly to reduce bug populations.
Sorghum Downy Mildew :

Detection: Monitor jowar leaves and stems for signs of downy mildew infection, such as yellowing, wilting, or mold growth.
Control: Apply fungicides targeted at downy mildew pathogens during early disease development stages. Implement cultural practices such as crop rotation, avoiding excessive irrigation, promoting air circulation, and using disease-resistant jowar varieties where available.
''')



pest_control()
