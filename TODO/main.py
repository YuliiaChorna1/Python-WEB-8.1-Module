from models import Notes
import connect


print('--- All notes ---')
notes = Notes.objects()
for note in notes:
    records = [f'description: {record.description}, done: {record.done}' for record in note.records]
    tags = [tag.name for tag in note.tags]
    print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")

print('--- Notes with tag Fun ---')

notes = Notes.objects(tags__name='Fun')
for note in notes:
    records = [f'description: {record.description}, done: {record.done}' for record in note.records]
    tags = [tag.name for tag in note.tags]
    print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")

print('--- Notes with tags Fun and Purchases ---')

notes = Notes.objects(tags__name__in=['Fun', 'Purchases'])
for note in notes:
    records = [f'description: {record.description}, done: {record.done}' for record in note.records]
    tags = [tag.name for tag in note.tags]
    print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")

# Оновлення 

# _id = '662d01f45f29a385de55da60'
# note = Notes.objects(id=_id)
# note.update(name='New Shopping') 

# Bидалення даних

# _id = '662d01f45f29a385de55da60'
# note = Notes.objects(id=_id).delete()
