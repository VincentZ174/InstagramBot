from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class Bot():

	links = []

	def __init__(self):
		self.login('USERNAME', 'PASSWORD')
		self.like_by_hashtag('programming')

	def login(self, username, password):
		self.driver = webdriver.Firefox()
		self.driver.get('https://instagram.com')
		sleep(3)
		username_input = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
		username_input.send_keys(username)
		sleep(1)
		password_input = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
		password_input.send_keys(password)
		sleep(1)
		self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]').click()
		sleep(3)
		self.driver.find_element(By.XPATH, "//button[text()='Not Now']").click()
		sleep(3)
		self.driver.find_element(By.XPATH, "//button[text()='Not Now']").click()


	def like_by_hashtag(self, hashtag):
		self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
		links = self.driver.find_elements_by_tag_name('a')

		def condition(link):
			return '.com/p/' in link.get_attribute('href')

		valid_links = list(filter(condition, links))

		for i in range(5):
			link = valid_links[i].get_attribute('href')
			if link not in self.links:
				self.links.append(link)

		for link in self.links:
			self.driver.get(link)
			sleep(3)
			self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button").click()
			sleep(5)

def main():
	while True:
		my_bot = Bot()
		sleep(60*60)

if __name__ == '__main__':
	main()