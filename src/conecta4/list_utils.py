def find_streak(haystack, needle, streak):
  assert streak > 0
  are_consecutive = False
  contador = 0
  for element in haystack:
    if element == needle:
      are_consecutive = True
      contador += 1
      if contador == streak:
        break
    else:
      #este es opcional se puede quitar ya que es implicito, si no es igual a la
      #aguja se queda en falso y contador se resetea a 0
      are_consecutive = False
      contador = 0


  return contador == streak






def get_nths(lol, n) -> list:
  assert n >= 1

  nths = []

  for sublist in lol:
    if len(sublist) < n: # mínimo tiene que tener n
      nths.append(None)
    else:
      nths.append(sublist[n - 1])

  return nths



def transpose_matrix(lol)-> list[list[int|float]]:
  result = []
  
  for i in range(len(lol[0])):
    row = get_nths(lol, i + 1)
    result.append(row)
  
  return result
  



def extend_list(elements: list, distance: int, filler) -> list:
  result = []
  
  for elm in elements:
    result.append(elm)
  for i in range(distance):
    result.append(filler)

  return result



def extend_lol(lol: list[list], filler) ->list[list]:
  """
  Aplica extend_list a cada sublista del lol y me devuelve un nuevo lol
  """
  result = []
  for i, sublist in enumerate(lol):
    result.append(extend_list(sublist), i, filler)

  return result

def add_prefix(elements:list, number: int, filler: any)->any:
    """
    recibe una lista y devuelve una nueva lista con number rellenos 
    al principio (un prefijo):
    add_prefix([1,2], 2, None) -> [None, None, 1,2]
    """
    return ([filler] * number) + elements



def displace_list(elements: list, distance: int, total_size: int, filler)->list:
    """
    Crea una nueva lista de tamaño total_size, con la original, desplazada
    hacia en final distance posiciones.
    Los espacios nueos se rellenan con filler
    displace_list([1,2,3], 1, 7, None) -> [None, 1, 2, 3, None, None, None]
    """
    
    with_prefix = add_prefix(elements, distance, filler)
    suffix_distance = total_size - len(with_prefix)
    return with_prefix + ([filler] * suffix_distance)    



#print(displace_list([1,2,3], 4, 7, None))


def displace_lol(lol, filler):
  displaced = []
  base_size = len(lol[0])
  extended_size = base_size + len(lol) - 1
  
  for i, sublist in enumerate(lol):

      displaced.append(displace_list(sublist, i, extended_size, filler))
    
  return displaced

  